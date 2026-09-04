#!/usr/bin/env python3
"""Transport-neutral live-invocation interface + one concrete Playwright MCP
browser-session adapter for AIOS AutoResearch v0.2 (issue #413, parent #409).

Scope of this child:

- Define ONE narrow, transport-neutral invocation interface
  (`invoke(request, policy, budget, transport) -> LiveInvocationResult`).
- Provide ONE concrete browser-session transport
  (`PlaywrightMcpBrowserTransport`) for the single connection mode selected
  for v0.2 by the owner: a **dedicated persistent Playwright profile** the
  owner has signed in to interactively. No other mode is implemented here.
- Provide ONE deterministic `FakeBrowserTransport` for automated tests only.
- Enforce, in code, the #411 authority / budget / privacy / session rules
  before and after every browser invocation.
- Hand a schema-valid live record to the existing v0.1 shadow runner through
  its already-existing `AdapterCallable` seam
  (`scripts/autoresearch_shadow_runner.py`), without weakening isolation.

Hard boundaries (issue #413 Forbidden actions), enforced by construction:

- No semantic Judge call here (that is #414).
- No candidate mutation, benchmark batch, holdout access, active Project edit,
  or commit/push/PR/merge by this module.
- No credential automation: this module never types a password, reads a
  secret, or exports cookies / storage-state / a browser profile.
- No provider API/SDK/CLI path.
- No mock result is ever labelled `live`: `FakeBrowserTransport` results carry
  `transport_id == "fake_browser"` and `capture_method == "test_double"`.
- No claim of API- or ChatGPT-Project-UI equivalence: every result carries the
  fixed `limitations` string and `fidelity_mode == "repo_replay"`.

This module performs NO network or subprocess I/O of its own. The concrete
Playwright transport calls an injected `mcp_call` callable; automated tests
never provide one.
"""

from __future__ import annotations

import hashlib
import re
import time
import unicodedata
from dataclasses import dataclass, field
from typing import Callable, Optional, Protocol


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class LiveTransportError(RuntimeError):
    """A transport-level failure that `invoke` maps to an explicit non-pass
    `termination_status` -- never a silent success. Ordinary outcomes
    (timeout, lost session, wrong page) are reported through
    `LiveInvocationResult.termination_status`, not raised past `invoke`."""


class TransportTimeout(LiveTransportError):
    pass


class TransportSessionLost(LiveTransportError):
    pass


class TransportNavigationError(LiveTransportError):
    pass


# ---------------------------------------------------------------------------
# Vocabularies (kept small and closed on purpose)
# ---------------------------------------------------------------------------

TRANSPORT_MODES = frozenset({"dedicated_persistent_profile"})

TERMINATION_STATUSES = frozenset(
    {
        "completed",
        "timeout",
        "cancelled",
        "navigation_error",
        "session_lost",
        "authority_missing",
        "budget_exhausted",
        "context_mismatch",
        "wrong_target",
        "selector_unverified",
        "empty_response",
        "validation_error",
    }
)

#: Every value except "completed" is a non-pass outcome and can never become a
#: live observation PASS (issue #413: "never report a failed/unverified browser
#: action as a live observation PASS").
NON_PASS_TERMINATIONS = TERMINATION_STATUSES - {"completed"}

#: The comparator (#416 onward) must be able to tell these three apart. A
#: browser UI frequently exposes none of them; "not_observable" is the honest
#: value, never a guess from branding / default selector / URL / plan.
MODEL_IDENTITY_STATUSES = frozenset({"verified", "ui_observed", "not_observable"})

FIDELITY_LIMITATION = (
    "This context is a reproducible repository-derived replay of AI-OS "
    "instructions and governed sources. It is not evidence of exact "
    "equivalence to proprietary ChatGPT Project runtime assembly unless "
    "separately validated."
)


# ---------------------------------------------------------------------------
# Hashing / normalisation helpers
# ---------------------------------------------------------------------------


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalize_response(text: str) -> str:
    """Deterministic normalisation so identical captured answers hash
    identically: Unicode NFC, `\\r\\n` -> `\\n`, strip trailing spaces on each
    line, strip leading/trailing blank lines."""
    text = unicodedata.normalize("NFC", text).replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in text.split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def response_hash(normalized_text: str) -> str:
    return sha256_hex(normalized_text.encode("utf-8"))


def compute_request_hash(payload_text: str, context_hash: str) -> str:
    return sha256_hex(f"{context_hash}\n\n{payload_text}".encode("utf-8"))


# ---------------------------------------------------------------------------
# Privacy: fail-closed sanitisation of anything about to be persisted
# ---------------------------------------------------------------------------

_SECRET_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("cookie_header", re.compile(r"(?i)\bcookie\s*:\s*\S+")),
    ("set_cookie", re.compile(r"(?i)\bset-cookie\b")),
    ("authorization_header", re.compile(r"(?i)\bauthorization\s*:\s*\S+")),
    ("bearer_token", re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._\-]{12,}")),
    ("openai_key", re.compile(r"\bsk-[A-Za-z0-9]{16,}")),
    ("session_token_kv", re.compile(r"(?i)\b(session|access|refresh|id)[_-]?token\s*[=:]\s*\S+")),
    ("secret_kv", re.compile(r"(?i)\b(api[_-]?key|apikey|secret|token|passwd|password)\s*[=:]\s*\S+")),
    ("storage_state", re.compile(r"(?i)\b(localStorage|sessionStorage|storageState)\b")),
    ("pem_block", re.compile(r"-----BEGIN [A-Z ]+-----")),
    ("set_local_storage", re.compile(r"(?i)\b__Secure-|\b__Host-")),
)


def sanitization_flags(text: str) -> list[str]:
    """Names of every secret-shaped pattern found in `text`. A non-empty list
    means the text must NOT be persisted as-is."""
    return [name for name, pat in _SECRET_PATTERNS if pat.search(text or "")]


def redact(text: str) -> str:
    out = text or ""
    for _name, pat in _SECRET_PATTERNS:
        out = pat.sub("[REDACTED]", out)
    return out


# ---------------------------------------------------------------------------
# Value objects
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class TransportPolicy:
    """The predeclared, per-batch browser/session policy. Frozen: a case's
    untrusted task text can never mutate destination or transport config
    (issue #413 automated check)."""

    transport_id: str
    transport_version: str
    transport_mode: str
    target_product: str  # logical name, e.g. "openai_chatgpt_ui"
    target_url_prefix: str  # e.g. "https://chatgpt.com/"
    session_policy: str  # "fresh_conversation" | "reuse_conversation"
    browser_channel: str = "chromium"
    browser_session_ref: str = "not_captured"  # non-secret logical id/hash only
    expected_context_hash: Optional[str] = None
    expected_model_selector: Optional[str] = None
    #: Browser-session transports have no AutoResearch-side per-call fee. The
    #: owner's Phase 0 authorization is "$0 / plan-included only", so this stays
    #: False; a True here with a non-positive cost cap makes `invoke` refuse to
    #: submit.
    incremental_paid_cost: bool = False

    def __post_init__(self) -> None:
        if self.transport_mode not in TRANSPORT_MODES:
            raise LiveTransportError(
                f"unsupported transport_mode {self.transport_mode!r}; "
                f"v0.2 implements exactly one: {sorted(TRANSPORT_MODES)}"
            )
        if self.session_policy not in {"fresh_conversation", "reuse_conversation"}:
            raise LiveTransportError(f"unknown session_policy {self.session_policy!r}")


@dataclass
class BudgetState:
    """Mutable call/cost/time ledger for one batch. `invoke` reserves a call
    BEFORE submission and never releases it once the provider was actually
    reached (issue #411: every call, including retries, consumes budget)."""

    max_provider_calls: Optional[int]
    max_cost_amount: Optional[float]
    max_cost_currency: Optional[str]
    max_wall_clock_minutes: Optional[int] = None
    calls_used: int = 0
    cost_spent: float = 0.0
    _started_monotonic: float = field(default_factory=time.monotonic, repr=False)

    def authorization_ok(self) -> bool:
        """#411 rule the schema alone cannot express: a live batch is only
        authorised when a numeric call ceiling exists AND the cost cap is a
        real number with a currency (a `$0` plan-included cap is a real number:
        `0.0` + "USD")."""
        if self.max_provider_calls is None or self.max_provider_calls <= 0:
            return False
        if self.max_cost_amount is None or self.max_cost_currency in (None, ""):
            return False
        return True

    def calls_remaining(self) -> int:
        if self.max_provider_calls is None:
            return 0
        return max(self.max_provider_calls - self.calls_used, 0)

    def can_spend_call(self) -> bool:
        return self.authorization_ok() and self.calls_remaining() > 0

    def wall_clock_exceeded(self) -> bool:
        if self.max_wall_clock_minutes is None:
            return False
        return (time.monotonic() - self._started_monotonic) > self.max_wall_clock_minutes * 60

    def reserve_call(self) -> None:
        self.calls_used += 1

    def record_cost(self, amount: float) -> None:
        self.cost_spent += amount


@dataclass(frozen=True)
class LiveInvocationRequest:
    invocation_id: str
    experiment_id: str
    condition: str  # "baseline" | "candidate"
    case_id: str
    context_id: str
    context_hash: str
    payload_text: str
    authority_evidence_ref: str
    external_action_preview_ref: str = ""
    request_hash: Optional[str] = None
    retry_of: Optional[str] = None

    def with_request_hash(self) -> "LiveInvocationRequest":
        if self.request_hash:
            return self
        return LiveInvocationRequest(
            **{**self.__dict__, "request_hash": compute_request_hash(self.payload_text, self.context_hash)}
        )


@dataclass(frozen=True)
class RawCapture:
    response_text: str
    observed_model_selector: Optional[str]
    page_url: Optional[str]
    started_at: float
    completed_at: float


@dataclass(frozen=True)
class LiveInvocationResult:
    invocation_id: str
    experiment_id: str
    condition: str
    case_id: str
    transport_id: str
    transport_version: str
    transport_mode: str
    browser_channel: str
    browser_session_ref: str
    target_product: str
    provider: str
    model: str
    model_version_or_snapshot: str
    model_identity_status: str
    runtime_version: str
    context_id: str
    context_hash: str
    request_hash: str
    sampling_configuration: dict
    started_at: float
    completed_at: float
    latency_ms: int
    termination_status: str
    response_text_or_ref: Optional[str]
    response_hash: Optional[str]
    input_tokens: str
    output_tokens: str
    usage_metadata_status: str
    cost_amount: float
    cost_currency: str
    retry_of: Optional[str]
    external_action_preview_ref: str
    authority_evidence_ref: str
    redaction_status: str
    capture_method: str
    fidelity_mode: str
    limitations: str

    @property
    def is_pass(self) -> bool:
        return self.termination_status == "completed" and bool(self.response_hash)


# ---------------------------------------------------------------------------
# Transport protocol + implementations
# ---------------------------------------------------------------------------


class BrowserSessionTransport(Protocol):
    transport_id: str
    transport_version: str
    capture_method: str

    def open_session(self, policy: TransportPolicy) -> object: ...
    def verify_target(self, handle: object, policy: TransportPolicy) -> bool: ...
    def read_model_selector(self, handle: object, policy: TransportPolicy) -> Optional[str]: ...
    def submit(self, handle: object, payload_text: str, timeout_seconds: int) -> RawCapture: ...
    def close_session(self, handle: object) -> None: ...


class FakeBrowserTransport:
    """Deterministic test double. NEVER performs I/O. `transport_id` and
    `capture_method` are fixed so a fake result can never be mistaken for
    `live`."""

    transport_id = "fake_browser"
    transport_version = "test-double"
    capture_method = "test_double"

    def __init__(
        self,
        *,
        scripted_response: str = "OK: repo-replay smoke answer.",
        observed_selector: Optional[str] = None,
        behavior: str = "ok",
        page_url: str = "https://chatgpt.com/c/fake",
    ) -> None:
        # behavior in {"ok","timeout","navigation_error","session_lost","wrong_target","empty"}
        self.scripted_response = scripted_response
        self.observed_selector = observed_selector
        self.behavior = behavior
        self.page_url = page_url
        self.submissions = 0

    def open_session(self, policy: TransportPolicy) -> dict:
        if self.behavior == "session_lost":
            raise TransportSessionLost("fake: session could not be opened")
        return {"opened": True}

    def verify_target(self, handle: object, policy: TransportPolicy) -> bool:
        if self.behavior == "navigation_error":
            raise TransportNavigationError("fake: navigation failed")
        if self.behavior == "wrong_target":
            return False
        return self.page_url.startswith(policy.target_url_prefix)

    def read_model_selector(self, handle: object, policy: TransportPolicy) -> Optional[str]:
        return self.observed_selector

    def submit(self, handle: object, payload_text: str, timeout_seconds: int) -> RawCapture:
        self.submissions += 1
        started = 1_000.0
        if self.behavior == "timeout":
            raise TransportTimeout(f"fake: no response within {timeout_seconds}s")
        if self.behavior == "session_lost":
            raise TransportSessionLost("fake: session dropped mid-submit")
        text = "" if self.behavior == "empty" else self.scripted_response
        return RawCapture(
            response_text=text,
            observed_model_selector=self.observed_selector,
            page_url=self.page_url,
            started_at=started,
            completed_at=started + 1.5,
        )

    def close_session(self, handle: object) -> None:
        return None


class PlaywrightMcpBrowserTransport:
    """The one concrete v0.2 transport: a dedicated persistent Playwright MCP
    profile the owner has already signed in to.

    `mcp_call(tool_name, arguments) -> dict` is injected. It is expected to
    proxy to the real `mcp__playwright__browser_*` tools. Automated tests never
    pass one; calling `submit` without it raises `LiveTransportError` rather
    than fabricating a response.

    This class does not sign in, does not read cookies/storage, and does not
    inspect any tab other than the one it navigates.
    """

    transport_id = "playwright_mcp"
    capture_method = "browser_automation"

    def __init__(
        self,
        *,
        mcp_call: Optional[Callable[[str, dict], dict]] = None,
        transport_version: str = "playwright-mcp/latest",
        response_extract_js: Optional[str] = None,
        selector_extract_js: Optional[str] = None,
    ) -> None:
        self._mcp = mcp_call
        self.transport_version = transport_version
        self._response_extract_js = response_extract_js
        self._selector_extract_js = selector_extract_js

    def _require_mcp(self) -> Callable[[str, dict], dict]:
        if self._mcp is None:
            raise LiveTransportError(
                "PlaywrightMcpBrowserTransport has no mcp_call binding; "
                "refusing to fabricate a browser response. Wire the real "
                "mcp__playwright__browser_* tools for the live smoke."
            )
        return self._mcp

    def open_session(self, policy: TransportPolicy) -> dict:
        mcp = self._require_mcp()
        mcp("browser_navigate", {"url": policy.target_url_prefix})
        return {"navigated_to": policy.target_url_prefix}

    def verify_target(self, handle: object, policy: TransportPolicy) -> bool:
        mcp = self._require_mcp()
        snap = mcp("browser_snapshot", {})
        url = str(snap.get("url", "")) if isinstance(snap, dict) else ""
        if not url:
            raise TransportNavigationError("no URL in browser_snapshot result")
        return url.startswith(policy.target_url_prefix)

    def read_model_selector(self, handle: object, policy: TransportPolicy) -> Optional[str]:
        if not self._selector_extract_js:
            return None
        mcp = self._require_mcp()
        res = mcp("browser_evaluate", {"function": self._selector_extract_js})
        val = res.get("result") if isinstance(res, dict) else None
        return str(val) if val not in (None, "") else None

    def submit(self, handle: object, payload_text: str, timeout_seconds: int) -> RawCapture:
        mcp = self._require_mcp()
        started = time.monotonic()
        mcp("browser_type", {"text": payload_text, "submit": True, "element": "chat input", "ref": "composer"})
        try:
            mcp("browser_wait_for", {"textGone": "Stop generating", "time": timeout_seconds})
        except Exception as exc:  # noqa: BLE001 - normalise any wait failure
            raise TransportTimeout(f"wait_for did not settle within {timeout_seconds}s: {exc}") from exc
        if self._response_extract_js:
            res = mcp("browser_evaluate", {"function": self._response_extract_js})
            text = str(res.get("result", "")) if isinstance(res, dict) else ""
        else:
            snap = mcp("browser_snapshot", {})
            text = str(snap.get("last_message", "")) if isinstance(snap, dict) else ""
        snap2 = mcp("browser_snapshot", {})
        url = str(snap2.get("url", "")) if isinstance(snap2, dict) else None
        return RawCapture(
            response_text=text,
            observed_model_selector=None,
            page_url=url,
            started_at=started,
            completed_at=time.monotonic(),
        )

    def close_session(self, handle: object) -> None:
        # Deliberately does NOT close the owner's browser or profile; a live
        # batch leaves the session as it found it.
        return None


# ---------------------------------------------------------------------------
# Preview (PLAN -> PREVIEW EFFECT, AES §13.2) -- no I/O
# ---------------------------------------------------------------------------


def preview_external_action(request: LiveInvocationRequest, policy: TransportPolicy) -> dict:
    req = request.with_request_hash()
    return {
        "action_class": "live_browser_model_call",
        "invocation_id": req.invocation_id,
        "experiment_id": req.experiment_id,
        "condition": req.condition,
        "case_id": req.case_id,
        "transport_id": policy.transport_id,
        "transport_mode": policy.transport_mode,
        "target_product": policy.target_product,
        "target_url_prefix": policy.target_url_prefix,
        "session_policy": policy.session_policy,
        "context_id": req.context_id,
        "context_hash": req.context_hash,
        "request_hash": req.request_hash,
        "expected_model_selector": policy.expected_model_selector,
        "authority_evidence_ref": req.authority_evidence_ref,
        "note": "preview only; not authorization (AES §13.2, live-contract §5).",
    }


# ---------------------------------------------------------------------------
# The one narrow invocation interface
# ---------------------------------------------------------------------------


def _provider_for(target_product: str) -> str:
    return {
        "openai_chatgpt_ui": "openai_chatgpt_ui",
        "anthropic_claude_ui": "anthropic_claude_ui",
    }.get(target_product, target_product or "not_observable")


def _result(
    *,
    request: LiveInvocationRequest,
    policy: TransportPolicy,
    transport: BrowserSessionTransport,
    termination_status: str,
    started_at: float,
    completed_at: float,
    response_text: Optional[str] = None,
    response_hash_hex: Optional[str] = None,
    observed_selector: Optional[str] = None,
    cost_currency: str = "not_applicable",
    limitations_extra: str = "",
) -> LiveInvocationResult:
    if termination_status not in TERMINATION_STATUSES:
        raise LiveTransportError(f"unknown termination_status {termination_status!r}")
    req = request.with_request_hash()
    if observed_selector:
        model, identity_status = observed_selector, "ui_observed"
    else:
        model, identity_status = "not_observable", "not_observable"
    redaction_status = "sanitized" if response_text is not None else "not_applicable"
    limitations = FIDELITY_LIMITATION
    if limitations_extra:
        limitations = f"{limitations} | {limitations_extra}"
    return LiveInvocationResult(
        invocation_id=req.invocation_id,
        experiment_id=req.experiment_id,
        condition=req.condition,
        case_id=req.case_id,
        transport_id=transport.transport_id,
        transport_version=transport.transport_version,
        transport_mode=policy.transport_mode,
        browser_channel=policy.browser_channel,
        browser_session_ref=policy.browser_session_ref,
        target_product=policy.target_product,
        provider=_provider_for(policy.target_product),
        model=model,
        model_version_or_snapshot="not_observable",
        model_identity_status=identity_status,
        runtime_version="not_observable",
        context_id=req.context_id,
        context_hash=req.context_hash,
        request_hash=req.request_hash or "",
        sampling_configuration={},
        started_at=started_at,
        completed_at=completed_at,
        latency_ms=max(int((completed_at - started_at) * 1000), 0),
        termination_status=termination_status,
        response_text_or_ref=response_text,
        response_hash=response_hash_hex,
        input_tokens="not_observable",
        output_tokens="not_observable",
        usage_metadata_status="not_observable",
        cost_amount=0.0,
        cost_currency=cost_currency,
        retry_of=req.retry_of,
        external_action_preview_ref=req.external_action_preview_ref,
        authority_evidence_ref=req.authority_evidence_ref,
        redaction_status=redaction_status,
        capture_method=transport.capture_method,
        fidelity_mode="repo_replay",
        limitations=limitations,
    )


def invoke(
    request: LiveInvocationRequest,
    policy: TransportPolicy,
    budget: BudgetState,
    transport: BrowserSessionTransport,
) -> LiveInvocationResult:
    """PLAN -> PREVIEW EFFECT -> AUTHORITY CHECK -> COMMIT -> VERIFY
    (AES §13.2, live-contract §5), applied to one browser model call.

    Returns a `LiveInvocationResult` for every path. A non-"completed"
    `termination_status` is never a PASS and always preserves a sanitized
    record. A browser submission only happens after every pre-submission gate
    passes.
    """
    now = time.monotonic()
    req = request.with_request_hash()

    # --- AUTHORITY CHECK (no submission on failure) ---
    if not req.authority_evidence_ref.strip():
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="authority_missing", started_at=now, completed_at=now,
            limitations_extra="no authority_evidence_ref supplied; live-contract §5/§10",
        )
    if not budget.authorization_ok():
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="authority_missing", started_at=now, completed_at=now,
            limitations_extra="budget not authorised (missing numeric call ceiling or cost cap+currency)",
        )

    # --- BUDGET (no submission on failure) ---
    if budget.wall_clock_exceeded():
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="budget_exhausted", started_at=now, completed_at=now,
            limitations_extra="max_wall_clock_minutes exceeded",
        )
    if not budget.can_spend_call():
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="budget_exhausted", started_at=now, completed_at=now,
            limitations_extra="max_provider_calls reached",
        )
    if policy.incremental_paid_cost and (budget.max_cost_amount or 0.0) <= 0.0:
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="budget_exhausted", started_at=now, completed_at=now,
            limitations_extra="transport would incur paid usage but cost cap is $0 (plan-included only)",
        )

    # --- CONTEXT IDENTITY (no submission on failure) ---
    if not req.context_hash.strip():
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="context_mismatch", started_at=now, completed_at=now,
            limitations_extra="request carries no context_hash",
        )
    if policy.expected_context_hash and req.context_hash != policy.expected_context_hash:
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="context_mismatch", started_at=now, completed_at=now,
            limitations_extra="context_hash != policy.expected_context_hash",
        )

    # --- COMMIT: open + verify + selector, then submit ---
    started = time.monotonic()
    try:
        handle = transport.open_session(policy)
    except TransportSessionLost as exc:
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="session_lost", started_at=started, completed_at=time.monotonic(),
            limitations_extra=f"open_session: {exc}",
        )
    try:
        try:
            on_target = transport.verify_target(handle, policy)
        except TransportNavigationError as exc:
            return _result(
                request=req, policy=policy, transport=transport,
                termination_status="navigation_error", started_at=started, completed_at=time.monotonic(),
                limitations_extra=f"verify_target: {exc}",
            )
        if not on_target:
            return _result(
                request=req, policy=policy, transport=transport,
                termination_status="wrong_target", started_at=started, completed_at=time.monotonic(),
                limitations_extra="verify_target returned False before submission",
            )

        observed_selector = transport.read_model_selector(handle, policy)
        if policy.expected_model_selector and observed_selector != policy.expected_model_selector:
            return _result(
                request=req, policy=policy, transport=transport,
                termination_status="selector_unverified", started_at=started, completed_at=time.monotonic(),
                observed_selector=observed_selector,
                limitations_extra=(
                    f"requested selector {policy.expected_model_selector!r} != "
                    f"observed {observed_selector!r}; no submission"
                ),
            )

        # This call reaches the provider: reserve budget BEFORE submitting and
        # never release it (issue #411: every call consumes budget).
        budget.reserve_call()
        try:
            capture = transport.submit(handle, req.payload_text, _timeout_seconds(policy, budget))
        except TransportTimeout as exc:
            return _result(
                request=req, policy=policy, transport=transport,
                termination_status="timeout", started_at=started, completed_at=time.monotonic(),
                limitations_extra=f"submit: {exc}",
            )
        except TransportSessionLost as exc:
            return _result(
                request=req, policy=policy, transport=transport,
                termination_status="session_lost", started_at=started, completed_at=time.monotonic(),
                limitations_extra=f"submit: {exc}",
            )
        except LiveTransportError as exc:
            return _result(
                request=req, policy=policy, transport=transport,
                termination_status="validation_error", started_at=started, completed_at=time.monotonic(),
                limitations_extra=f"submit: {exc}",
            )

        # --- VERIFY ---
        normalized = normalize_response(capture.response_text or "")
        if not normalized.strip():
            return _result(
                request=req, policy=policy, transport=transport,
                termination_status="empty_response", started_at=capture.started_at, completed_at=capture.completed_at,
                observed_selector=observed_selector,
                limitations_extra="captured response was empty after normalisation",
            )
        flags = sanitization_flags(normalized)
        if flags:
            return _result(
                request=req, policy=policy, transport=transport,
                termination_status="validation_error", started_at=capture.started_at, completed_at=capture.completed_at,
                observed_selector=observed_selector,
                limitations_extra=f"secret-shaped content in capture ({','.join(flags)}); not persisted",
            )
        return _result(
            request=req, policy=policy, transport=transport,
            termination_status="completed", started_at=capture.started_at, completed_at=capture.completed_at,
            response_text=normalized, response_hash_hex=response_hash(normalized),
            observed_selector=observed_selector or capture.observed_model_selector,
            cost_currency=budget.max_cost_currency or "not_applicable",
        )
    finally:
        try:
            transport.close_session(handle)
        except Exception:  # noqa: BLE001 - cleanup must not mask the result
            pass


def _timeout_seconds(policy: TransportPolicy, budget: BudgetState) -> int:
    # call_timeout_seconds lives on the batch config (#411 schema); the policy
    # object here is transport-shaped, so accept an attribute if present and
    # otherwise fall back to a conservative default.
    return int(getattr(policy, "call_timeout_seconds", 180) or 180)


# ---------------------------------------------------------------------------
# Integration seam with the v0.1 shadow runner
# ---------------------------------------------------------------------------


def to_observation_row(result: LiveInvocationResult) -> dict:
    """Adapt a `LiveInvocationResult` to the dict shape
    `scripts/autoresearch_shadow_runner.py`'s `AdapterCallable` contract
    expects: at least `response` and `runtime_model_configuration`. Extra
    keys (all live-provenance) pass through the runner untouched and are what
    the #414+ evidence layer and `schemas/autoresearch_live_invocation.schema.json`
    consume."""
    return {
        "experiment_id": result.experiment_id,
        "condition": result.condition,
        "case_id": result.case_id,
        "response": result.response_text_or_ref,
        "runtime_model_configuration": {
            "transport_id": result.transport_id,
            "transport_mode": result.transport_mode,
            "target_product": result.target_product,
            "provider": result.provider,
            "model": result.model,
            "model_identity_status": result.model_identity_status,
            "context_hash": result.context_hash,
            "sampling_configuration": result.sampling_configuration,
        },
        "provenance": "live" if result.transport_id != "fake_browser" else "synthetic_fixture",
        "capture_method": result.capture_method,
        "live_invocation_id": result.invocation_id,
        "live_termination_status": result.termination_status,
        "response_hash": result.response_hash,
        "request_hash": result.request_hash,
        "usage_metadata_status": result.usage_metadata_status,
        "cost_amount": result.cost_amount,
        "cost_currency": result.cost_currency,
        "limitations": result.limitations,
    }


def to_live_invocation_record(result: LiveInvocationResult) -> dict:
    """Serialise a `LiveInvocationResult` to a dict that validates against
    `schemas/autoresearch_live_invocation.schema.json`. Drops the internal
    monotonic timestamps (`started_at`/`completed_at`); `latency_ms` already
    carries the derived duration."""
    return {
        "schema_version": "0.2.0",
        "invocation_id": result.invocation_id,
        "experiment_id": result.experiment_id,
        "condition": result.condition,
        "case_id": result.case_id,
        "transport_id": result.transport_id,
        "transport_version": result.transport_version,
        "transport_mode": result.transport_mode,
        "browser_channel": result.browser_channel,
        "browser_session_ref": result.browser_session_ref,
        "target_product": result.target_product,
        "provider": result.provider,
        "model": result.model,
        "model_version_or_snapshot": result.model_version_or_snapshot,
        "model_identity_status": result.model_identity_status,
        "runtime_version": result.runtime_version,
        "context_id": result.context_id,
        "context_hash": result.context_hash,
        "request_hash": result.request_hash,
        "sampling_configuration": result.sampling_configuration,
        "latency_ms": result.latency_ms,
        "termination_status": result.termination_status,
        "response_text_or_ref": result.response_text_or_ref,
        "response_hash": result.response_hash,
        "input_tokens": result.input_tokens,
        "output_tokens": result.output_tokens,
        "usage_metadata_status": result.usage_metadata_status,
        "cost_amount": result.cost_amount,
        "cost_currency": result.cost_currency,
        "retry_of": result.retry_of,
        "external_action_preview_ref": result.external_action_preview_ref,
        "authority_evidence_ref": result.authority_evidence_ref,
        "redaction_status": result.redaction_status,
        "capture_method": result.capture_method,
        "fidelity_mode": result.fidelity_mode,
        "limitations": result.limitations,
    }


def live_browser_adapter_callable(
    *,
    requests_by_key: dict[tuple[str, str, str], LiveInvocationRequest],
    policy: TransportPolicy,
    budget: BudgetState,
    transport: BrowserSessionTransport,
    results_sink: Optional[list] = None,
):
    """Build an `AdapterCallable` -- `(experiment_id, condition, case_id) ->
    dict | None` -- for `run_shadow_experiment`.

    Returns the observation row only when the invocation `is_pass`; a non-pass
    invocation returns `None`, which the runner maps to its existing
    `MISSING_OBSERVATION -> inconclusive` path (a failed/unverified browser
    action never becomes a live PASS). Every `LiveInvocationResult`, pass or
    not, is appended to `results_sink` if provided, so the caller keeps the
    full audit trail."""

    def _adapter(experiment_id: str, condition: str, case_id: str) -> Optional[dict]:
        req = requests_by_key.get((experiment_id, condition, case_id))
        if req is None:
            return None
        result = invoke(req, policy, budget, transport)
        if results_sink is not None:
            results_sink.append(result)
        return to_observation_row(result) if result.is_pass else None

    return _adapter

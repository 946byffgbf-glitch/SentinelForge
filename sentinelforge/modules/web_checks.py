"""Passive web checks based on a normal response, not injected test payloads."""
from .http_audit import fetch_headers
SECURITY_HEADERS = ["Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options", "X-Frame-Options", "Referrer-Policy"]

def audit_headers(url: str):
    result = fetch_headers(url)
    headers = result["headers"]
    lower = {k.lower(): v for k, v in headers.items()}
    missing = [h for h in SECURITY_HEADERS if h.lower() not in lower]
    findings = [{"title": f"Missing {header}", "severity": "medium", "detail": f"Response lacks {header}.",
                "recommendation": f"Configure {header} appropriate for the application."} for header in missing]
    if result["url"].startswith("http://"):
        findings.append({"title":"HTTP without TLS", "severity":"high", "detail":"Final URL uses plain HTTP.", "recommendation":"Serve sensitive content over HTTPS and redirect HTTP."})
    return {"response": result, "findings": findings}

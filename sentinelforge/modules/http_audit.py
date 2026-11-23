"""HTTP metadata audit. Sends one GET request; no attack payloads."""
import requests

def fetch_headers(url: str, timeout=8):
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must begin with http:// or https://")
    response = requests.get(url, timeout=timeout, allow_redirects=True, headers={"User-Agent":"SentinelForge/0.1 (authorized audit)"})
    return {"url": response.url, "status": response.status_code, "headers": dict(response.headers),
            "content_type": response.headers.get("Content-Type", ""), "bytes_received": len(response.content)}

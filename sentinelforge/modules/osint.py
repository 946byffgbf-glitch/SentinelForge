"""Basic passive DNS metadata; does not enumerate third-party data sources."""
import socket
from .common import validate_host

def dns_summary(host: str):
    host = validate_host(host)
    result = {"host": host, "addresses": [], "reverse_names": []}
    try:
        result["addresses"] = sorted({entry[4][0] for entry in socket.getaddrinfo(host, None)})
    except socket.gaierror as exc:
        result["error"] = str(exc)
    for ip in result["addresses"]:
        try:
            result["reverse_names"].append(socket.gethostbyaddr(ip)[0])
        except (socket.herror, socket.gaierror):
            pass
    return result

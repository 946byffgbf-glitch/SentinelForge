"""Low-impact TCP connect scan over an explicit list of ports."""
import socket
from concurrent.futures import ThreadPoolExecutor
from .common import validate_host


DEFAULT_PORTS = [21, 22, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 8080, 8443]

def scan_tcp(host: str, ports=DEFAULT_PORTS, timeout: float = 0.5, workers: int = 16):
    host = validate_host(host)
    if len(ports) > 256 or any(not isinstance(p, int) or not 1 <= p <= 65535 for p in ports):
        raise ValueError("Ports must be valid integers; at most 256 ports per scan.")
    def probe(port):
        try:
            with socket.create_connection((host, port), timeout=timeout):
                return {"port": port, "state": "open"}
        except (TimeoutError, OSError):
            return {"port": port, "state": "closed_or_filtered"}
    with ThreadPoolExecutor(max_workers=max(1, min(workers, 32))) as pool:
        return sorted(pool.map(probe, ports), key=lambda row: row["port"])

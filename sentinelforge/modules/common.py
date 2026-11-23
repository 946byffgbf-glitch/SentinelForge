import ipaddress
import re

def validate_host(value: str) -> str:
    value = value.strip()
    if not value or len(value) > 253 or any(ch in value for ch in " /\\\t\n"):
        raise ValueError("Provide a hostname or IP address, not a URL or path.")
    try:
        ipaddress.ip_address(value)
        return value
    except ValueError:
        if not re.fullmatch(r"(?=.{1,253}$)(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)*[A-Za-z]{2,63}", value):
            raise ValueError("Invalid hostname or IP address.")
        return value

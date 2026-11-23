"""Scope record and discovery planning helper."""
from .common import validate_host

def plan(target, notes=""):
    return {"target":validate_host(target),"scope_notes":notes,
            "checks":["DNS resolution","explicit-port TCP check","HTTP headers (only if in scope)","manual verification and evidence capture"]}

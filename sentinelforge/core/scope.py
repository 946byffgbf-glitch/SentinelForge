from dataclasses import dataclass


@dataclass(frozen=True)
class Scope:
    target: str
    authorized: bool = False



def require_authorized(scope: Scope) -> None:
    if not scope.authorized:
        raise PermissionError("Set --authorized only after confirming you own or have written permission to test this target.")

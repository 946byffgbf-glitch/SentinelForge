from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any
import json


@dataclass
class Finding:
    module: str
    title: str
    severity: str
    detail: str
    recommendation: str = "Review and remediate if applicable."

@dataclass
class Report:
    target: str
    findings: list[Finding]
    metadata: dict[str, Any]
    created_at: str

    @classmethod
    def create(cls, target: str, findings: list[Finding], metadata=None):
        return cls(target, findings, metadata or {}, datetime.now(timezone.utc).isoformat())

    def to_dict(self):
        return {"target": self.target, "findings": [asdict(f) for f in self.findings],
                "metadata": self.metadata, "created_at": self.created_at}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

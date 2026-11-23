"""Save assessment data in JSON or a simple HTML summary."""
import json, html
from pathlib import Path

def save_json(data, destination):
    Path(destination).write_text(json.dumps(data,indent=2),encoding="utf-8")

def save_html(data, destination):
    rows=[]
    for finding in data.get("findings",[]):
        rows.append("<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>".format(*[html.escape(str(finding.get(k,""))) for k in ("severity","title","detail","recommendation")]))
    page="<!doctype html><meta charset='utf-8'><title>SentinelForge report</title><h1>SentinelForge</h1><p>Target: {}</p><table border='1'><thead><tr><th>Severity</th><th>Finding</th><th>Details</th><th>Recommendation</th></tr></thead><tbody>{}</tbody></table>".format(html.escape(str(data.get("target",""))),"".join(rows))
    Path(destination).write_text(page,encoding="utf-8")

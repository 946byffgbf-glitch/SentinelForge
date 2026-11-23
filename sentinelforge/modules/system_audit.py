"""Basic host posture facts; does not change system state."""
import platform, os

def summary():
    return {"platform":platform.platform(),"python":platform.python_version(),"machine":platform.machine(),
            "user_privileged_hint":(os.geteuid()==0 if hasattr(os,"geteuid") else None),
            "recommendation":"Use least privilege; keep OS and packages patched; enable host firewall."}

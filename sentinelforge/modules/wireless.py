"""Read-only wireless status helper. No packet capture, deauth, or credential collection."""
import platform, subprocess

def status():
    system=platform.system()
    if system=="Linux":
        cmd=["nmcli","-t","-f","DEVICE,TYPE,STATE","device"]
    elif system=="Darwin":
        cmd=["networksetup","-listallhardwareports"]
    else:
        return {"platform":system,"note":"Unsupported platform for this read-only helper."}
    try:
        proc=subprocess.run(cmd,capture_output=True,text=True,timeout=4,check=False)
        return {"platform":system,"returncode":proc.returncode,"output":proc.stdout[:5000],"error":proc.stderr[:1000]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"platform":system,"error":str(exc),"note":"Install the platform utility or inspect wireless status manually."}

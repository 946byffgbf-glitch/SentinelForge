import argparse, json, logging
from .utils.logging_config import configure_logging
from .core.scope import Scope, require_authorized
from .modules import network, osint, http_audit, web_checks, password_audit, wireless, payload_lab, system_audit, recon, vulnerability_audit, reporting
log=logging.getLogger("sentinelforge")

def build_parser():
    parser=argparse.ArgumentParser(prog="sentinelforge",description="Defensive security assessment helpers. Use only on authorized systems.")
    parser.add_argument("--verbose",action="store_true")
    sub=parser.add_subparsers(dest="command",required=True)
    p=sub.add_parser("scan",help="TCP connect scan of selected ports"); p.add_argument("host"); p.add_argument("--ports",default="22,80,443,8080"); p.add_argument("--authorized",action="store_true")
    p=sub.add_parser("dns",help="Basic DNS metadata lookup"); p.add_argument("host")
    p=sub.add_parser("http",help="Fetch response metadata"); p.add_argument("url"); p.add_argument("--authorized",action="store_true")
    p=sub.add_parser("web-audit",help="Passive HTTP security-header checks"); p.add_argument("url"); p.add_argument("--authorized",action="store_true")
    p=sub.add_parser("password",help="Offline password-strength estimate"); p.add_argument("password")
    p=sub.add_parser("wireless",help="Read-only wireless adapter status")
    p=sub.add_parser("payload-lab",help="Show benign test markers")
    p=sub.add_parser("system",help="Host posture summary")
    p=sub.add_parser("recon-plan",help="Create a scoped discovery plan"); p.add_argument("target"); p.add_argument("--notes",default="")
    p=sub.add_parser("permissions",help="Check paths for world-writable permission"); p.add_argument("paths",nargs="+")
    p=sub.add_parser("report-demo",help="Write example report in JSON or HTML"); p.add_argument("output"); p.add_argument("--format",choices=["json","html"],default="json")
    return parser

def main(argv=None):
    args=build_parser().parse_args(argv); configure_logging(args.verbose if hasattr(args,"verbose") else False)
    try:
        if args.command=="scan":
            require_authorized(Scope(args.host,args.authorized)); ports=[int(p) for p in args.ports.split(",")]; result=network.scan_tcp(args.host,ports)
        elif args.command=="dns": result=osint.dns_summary(args.host)
        elif args.command=="http":
            require_authorized(Scope(args.url,args.authorized)); result=http_audit.fetch_headers(args.url)
        elif args.command=="web-audit":
            require_authorized(Scope(args.url,args.authorized)); result=web_checks.audit_headers(args.url)
        elif args.command=="password": result=password_audit.estimate_password(args.password)
        elif args.command=="wireless": result=wireless.status()
        elif args.command=="payload-lab": result=payload_lab.harmless_markers()
        elif args.command=="system": result=system_audit.summary()
        elif args.command=="recon-plan": result=recon.plan(args.target,args.notes)
        elif args.command=="permissions": result=vulnerability_audit.audit_local_permissions(args.paths)
        elif args.command=="report-demo":
            data={"target":"example.local","findings":[{"severity":"info","title":"Demo finding","detail":"Sample output only","recommendation":"Replace with evidence."}]}
            if args.format=="json": reporting.save_json(data,args.output)
            else: reporting.save_html(data,args.output)
            result={"saved":args.output,"format":args.format}
        else: raise RuntimeError("Unknown command")
        print(json.dumps(result,indent=2,ensure_ascii=False)); return 0
    except (ValueError, PermissionError) as exc:
        log.error("%s",exc); return 2
    except Exception as exc:
        log.exception("Unexpected error: %s",exc); return 1
if __name__=="__main__":
    raise SystemExit(main())

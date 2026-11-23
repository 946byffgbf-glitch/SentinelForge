# SentinelForge 🛡️

A modular Python command-line toolkit for **authorized defensive security assessments**. It combines lightweight host/network facts, DNS metadata, passive web response checks, local posture helpers, and report output into one CLI.


> **Ethics and scope:** Only run checks against systems you own or have explicit written permission to assess. The `--authorized` flag is an operator confirmation, not a legal authorization. Network commands are deliberately limited and non-destructive. This project does not implement credential guessing, password spraying, exploit execution, reverse shells, privilege-escalation automation, wireless disruption, or injected SQLi/XSS payload attacks.


## Features

- TCP connect checks over an explicit, capped port list
- Basic DNS resolution and reverse-name lookup
- HTTP response metadata and passive security-header checks
- Offline password-strength estimate (input stays local)
- Read-only wireless adapter status helper for Linux/macOS
- Local world-writable path audit
- Host posture summary and scoped recon plan
- JSON/HTML demo report generation
- Logging, validation, and unit tests


## Requirements

- Python 3.10+
- Linux or macOS
- `requests`
- For wireless status: Linux `nmcli` (NetworkManager) or macOS `networksetup`

## Install

```bash
git clone https://github.com/yourname/sentinelforge.git
cd sentinelforge
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -e .
```

Windows is not currently a supported target.

## Usage

```bash
sentinelforge --help
sentinelforge scan example.com --ports 22,80,443 --authorized
sentinelforge dns example.com
sentinelforge http https://example.com --authorized
sentinelforge web-audit https://example.com --authorized
sentinelforge password 'LongPassphrase!123'
sentinelforge wireless
sentinelforge payload-lab
sentinelforge system
sentinelforge recon-plan example.com --notes 'Owned test environment'
sentinelforge permissions ~/.ssh ~/.config
sentinelforge report-demo ./report.html --format html
```

The scanner uses TCP connect checks only and allows up to 256 specified ports. Network scans and HTTP requests require `--authorized` confirmation. DNS and local checks are informational and do not require that flag.


## Modules

| Module | CLI | Notes |
|---|---|---|
| Network scanning | `scan` | Explicit TCP ports, low-impact connect scan |
| OSINT | `dns` | DNS A/AAAA resolution and reverse lookup only |
| Vulnerability audit | `permissions` | Local file mode checks, not a CVE scanner |
| HTTP analysis | `http` | Single ordinary GET for response metadata |
| Web security | `web-audit` | Passive header checks and HTTP-vs-HTTPS warning |
| Wireless audit | `wireless` | Read-only local adapter status |
| Password audit | `password` | Local entropy estimate, not cracking |
| Payload lab | `payload-lab` | Benign, display-only markers for training |
| System audit | `system` | Host and Python facts |
| Recon planner | `recon-plan` | Scope notes and suggested defensive checks |
| Reporting | `report-demo` | Sample JSON or HTML output |

## Reports

```bash
sentinelforge report-demo report.json --format json
sentinelforge report-demo report.html --format html
```

The report command produces sample data so you can verify the output pipeline. Results from individual checks can be saved by redirecting CLI output or incorporated into your own scripts.


## Tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
sentinelforge/
├── README.md
├── pyproject.toml
├── requirements.txt
├── config/example.json
├── sentinelforge/
│   ├── cli.py
│   ├── core/ (scope and reporting primitives)
│   ├── modules/ (individual audit modules)
│   └── utils/ (logging)
└── tests/
```

## Contribution guidelines

1. Open an issue describing the defensive use case and scope.
2. Keep checks non-destructive and opt-in.
3. Avoid collecting credentials, personal data, or secrets.
4. Add validation, useful error messages, and unit tests for new modules.
5. Document limitations, dependencies, and examples.
6. Run the test suite before opening a pull request.

## Limitations

This is a starter assessment framework, not a replacement for professional scanners. Its checks are intentionally conservative. It does not provide full Nmap integration, CVE database correlation, active SQL injection/XSS testing, brute-force tooling, Metasploit automation, wireless attack workflows, or exploit/payload execution. Findings should be manually verified.


## License
MIT. See `LICENSE`.

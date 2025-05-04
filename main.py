
---

### `main.py`

```python
from scanner.port_scanner import scan_ports
from scanner.http_scanner import scan_http_headers
from scanner.dir_scanner import scan_common_dirs
import sys

if len(sys.argv) < 2:
    print("Uso: python main.py <url>")
    exit()

target_url = sys.argv[1]

print(f"🔍 initializing analysis of: {target_url}")

open_ports = scan_ports(target_url)
http_issues = scan_http_headers(target_url)
dirs_found = scan_common_dirs(target_url)

with open("reports/example_report.txt", "w") as report:
    report.write(f"safety report for: {target_url}\n\n")
    report.write(f"✅ open doors: {open_ports}\n")
    report.write(f"⚠️ insecure headers: {http_issues}\n")
    report.write(f"📂 directories found: {dirs_found}\n")

print("\n✅ report saved in: reports/example_report.txt")

import requests

def scan_common_dirs(url):
    print("🛠️ checking common directories...")
    dirs = ["/admin", "/login", "/dashboard", "/config"]
    found = []

    for d in dirs:
        try:
            full_url = url.rstrip("/") + d
            res = requests.get(full_url, timeout=2)
            if res.status_code == 200:
                found.append(d)
        except:
            continue

    return found

import requests

def scan_http_headers(url):
    print("🛠️ parsing HTTP headers...")
    issues = []
    try:
        res = requests.get(url, timeout=3)
        headers = res.headers

        if "X-Frame-Options" not in headers:
            issues.append("Falta X-Frame-Options")
        if "Content-Security-Policy" not in headers:
            issues.append("Falta Content-Security-Policy")
        if "Strict-Transport-Security" not in headers:
            issues.append("Falta HSTS")

    except Exception as e:
        issues.append(f"Erro ao acessar headers: {str(e)}")
    return issues

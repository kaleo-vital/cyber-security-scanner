import socket

def scan_ports(host):
    print("🛠️ checking open ports...")
    open_ports = []
    for port in [21, 22, 23, 80, 443, 3306, 8080]:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((host.replace("https://", "").replace("http://", ""), port))
            open_ports.append(port)
            sock.close()
        except:
            pass
    return open_ports

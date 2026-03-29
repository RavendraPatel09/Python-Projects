import socket
import time

class ConnectivityChecker:
    def __init__(self, targets):
        self.targets = targets

    def is_online(self, host):
        try:
            socket.setdefaulttimeout(3)
            host_ip = socket.gethostbyname(host)
            s = socket.create_connection((host_ip, 80), 2)
            s.close()
            return True
        except Exception:
            return False

    def monitor(self, rounds=5):
        for _ in range(rounds):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            for target in self.targets:
                status = "Online" if self.is_online(target) else "Offline"
                print(f"{timestamp} - {target}: {status}")
            time.sleep(5)

def main():
    sites = [
        "google.com",
        "github.com",
        "stackoverflow.com",
        "this-is-a-fake-site-123.com"

    ]
    checker = ConnectivityChecker(sites)
    checker.monitor()
if __name__ == "__main__":
    main()
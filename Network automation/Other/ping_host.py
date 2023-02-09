import subprocess
from pprint import pprint
import platform


def ping_ip_list(ip_list):
    pingable = []
    unpingable = []
    if platform.system().lower() == "windows":
        cmd = ["ping", "-n", "1"]
    else:
        cmd = ["ping", "-c", "1"]
    process = []
    for ip in ip_list:
        p = subprocess.Popen(cmd + [ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, encoding="utf-8")
        process.append(p)
        print(process)
    for ip, process in zip(ip_list, process):
        returncode = process.wait()
        if returncode == 0:
            pingable.append(ip)
        else:
            unpingable.append(ip)
    return pingable, unpingable


if __name__ == "__main__":
    ip_list = ["8.8.8.8", "192.168.1.1","1.2.3.4"]
    result = ping_ip_list(ip_list)
    ping,not_ping=result
    pprint(ping)
    pprint(not_ping)
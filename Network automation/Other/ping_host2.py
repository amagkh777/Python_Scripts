import subprocess
import ipaddress
from tabulate import tabulate


def ping_ip_list(ip_list):
    pingable = []
    unpingable = []
    cmd = ["ping", "-n", "1"]
    process = []
    for ip in ip_list:
        p = subprocess.Popen(cmd + [ip], stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL, encoding="utf-8")
        process.append(p)

    for ip, process in zip(ip_list, process):
        returncode = process.wait()
        if returncode == 0:
            pingable.append(ip)
        else:
            unpingable.append(ip)
    return pingable, unpingable


def convert_ranges_to_ip_list(ip_convert):
    result = []
    for ip in ip_convert:
        if "-" not in ip:
            result.append(ip)
        else:
            start_ip, stop_ip = ip.split("-")
            if "." not in stop_ip:
                stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for ip_adr in range(int(start_ip), int(stop_ip) + 1):
                result.append(str(ipaddress.ip_address(ip_adr)))
    return result
def  print_ip_table(ip_list):
    reach,unreach=ip_list
    d={'Reachable':reach,'Unreachable':unreach}
    print(tabulate(d, headers="keys"))


if __name__ == "__main__":
    ip_list = ["8.8.8.8", "10.1.1.1-10", "10.2.1.1-10.2.1.10"]
    result = convert_ranges_to_ip_list(ip_list)
    result_final=(ping_ip_list(result))

    print_ip_table(result_final)

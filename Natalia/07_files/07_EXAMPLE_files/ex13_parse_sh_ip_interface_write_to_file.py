from pprint import pprint

result = {}
output = ""

with open("sh_ip_interface.txt") as f:
    for line in f:
        words = line.split()
        if "line protocol is" in line:
            intf = words[0]
        elif "Internet address" in line:
            ip = words[-1]
        elif "MTU is" in line:
            mtu = words[2]
            output += f"{intf:20}{ip:20}{mtu:5}\n"

with open("intf_ip_mtu.txt", "w") as f:
    f.write(output)

"""
Example:

Ethernet0/0         192.168.100.1/24    1500 
Ethernet0/1         192.168.200.1/24    1500 
Ethernet0/2         19.1.1.1/24         1500 
Ethernet0/3         192.168.230.1/24    1500 
Loopback0           4.4.4.4/32          1514 

"""
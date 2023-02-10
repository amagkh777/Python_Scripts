result = {}

with open("sh_ip_interface.txt") as f:
    for line in f:
        if "line protocol" in line:
            interface = line.split()[0]
        elif "MTU is" in line:
            mtu = line.split()[-2]
            result[interface] = mtu

print(result)
"""
Example:

{'Ethernet0/0': '1500', 'Ethernet0/1': '1500', 'Ethernet0/2': '1500', 'Ethernet0/3': '1500', 'Loopback0': '1514'}

"""

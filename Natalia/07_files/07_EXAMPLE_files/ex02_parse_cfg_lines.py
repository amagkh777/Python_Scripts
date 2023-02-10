from pprint import pprint

result = {}

with open("config_r1.txt") as f:
    for line in f:
        if line.startswith("interface"):
            intf = line.split()[-1]
            result[intf] = None
        elif line.startswith(" ip address"):
            ip = line.split()[-2]
            result[intf] = ip

pprint(result)


"""
Example:

{'Ethernet0/0': '10.0.13.1',
 'Ethernet0/1': None,
 'Ethernet0/2': '10.0.19.1',
 'Ethernet0/3': None,
 'Ethernet0/3.100': None,
 'Ethernet1/0': None,
 'Loopback0': '10.1.1.1',
 'Tunnel0': None}
 
 """
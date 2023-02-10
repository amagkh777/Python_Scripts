from pprint  import pprint

files = ["files/config_r1.txt", "files/config_sw1.txt", "files/config_sw2.txt"]

output = []

for filename in files:
    with open(filename) as f:
        for line in f:
            words = line.split()
            if "hostname" in line:
                host = words[-1]
            elif line.startswith("interface"):
                interface = words[-1]
            elif line.startswith(" ip address"):
                ip = words[-2]
                output.append([host, interface, ip])
            elif "router ospf" in line or "alias" in line:
                break

pprint(output)

"""
Example:

[['PE_r1', 'Loopback0', '10.1.1.1'],
 ['PE_r1', 'Ethernet0/0', '10.0.13.1'],
 ['PE_r1', 'Ethernet0/2', '10.0.19.1'],
 ['sw1', 'Vlan100', '10.0.100.1'],
 ['sw2', 'Vlan100', '10.0.100.2']]
 
 """
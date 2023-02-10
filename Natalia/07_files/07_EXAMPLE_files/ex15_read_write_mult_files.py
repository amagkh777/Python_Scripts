from pprint import pprint


files = ["config_r1.txt", "config_sw1.txt", "config_sw2.txt"]

result = {}

for filename in files:
    with open(filename) as f:
        hostname = filename
        for line in f:
            if line.startswith("hostname"):
                hostname = line.split()[-1]
                result[hostname] = []
                print(hostname)
            elif line.startswith("interface"):
                if hostname not in result:
                    result[hostname] = []
                print(line.rstrip())
                intf = line.split()[-1]
                result[hostname].append(intf)

pprint(result)


"""
Example:

PE_r1
interface Loopback0
interface Tunnel0
interface Ethernet0/0
interface Ethernet0/1
interface Ethernet0/2
interface Ethernet0/3
interface Ethernet0/3.100
interface Ethernet1/0
sw1
interface FastEthernet0/0
interface FastEthernet0/1
interface FastEthernet0/2
interface FastEthernet0/3
interface FastEthernet1/0
interface FastEthernet1/1
interface FastEthernet1/2
interface FastEthernet1/3
interface Vlan100
sw2
interface FastEthernet0/0
interface FastEthernet0/1
interface FastEthernet0/2
interface FastEthernet0/3
interface FastEthernet1/0
interface FastEthernet1/1
interface FastEthernet1/2
interface FastEthernet1/3
interface FastEthernet2/0
interface FastEthernet2/1
interface Vlan100
{'PE_r1': ['Loopback0',
           'Tunnel0',
           'Ethernet0/0',
           'Ethernet0/1',
           'Ethernet0/2',
           'Ethernet0/3',
           'Ethernet0/3.100',
           'Ethernet1/0'],
 'sw1': ['FastEthernet0/0',
         'FastEthernet0/1',
         'FastEthernet0/2',
         'FastEthernet0/3',
         'FastEthernet1/0',
         'FastEthernet1/1',
         'FastEthernet1/2',
         'FastEthernet1/3',
         'Vlan100'],
 'sw2': ['FastEthernet0/0',
         'FastEthernet0/1',
         'FastEthernet0/2',
         'FastEthernet0/3',
         'FastEthernet1/0',
         'FastEthernet1/1',
         'FastEthernet1/2',
         'FastEthernet1/3',
         'FastEthernet2/0',
         'FastEthernet2/1',
         'Vlan100']}

"""


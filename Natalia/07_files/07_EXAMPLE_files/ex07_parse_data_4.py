from pprint import pprint


files = ["config_r1.txt", "config_sw1.txt", "config_sw2.txt"]

result = {}

for filename in files:
    with open(filename) as f:
        for line in f:
            if line.startswith("hostname"):
                hostname = line.split()[-1]
                print(hostname)
                result[hostname] = {}
            elif line.startswith("interface"):
                intf = line.split()[-1]
                print(intf)
                result[hostname][intf] = None
            elif line.strip().startswith("description"):
                desc = line.strip().lstrip("description ")
                # result[hostname][intf] = desc
                del result[hostname][intf]


pprint(result)

"""
Example:
{'PE_r1': {'Ethernet0/1': None,
           'Ethernet0/3.100': None,
           'Ethernet1/0': None,
           'Loopback0': None,
           'Tunnel0': None},
 'sw1': {'FastEthernet0/0': None,
         'FastEthernet0/1': None,
         'FastEthernet0/2': None,
         'FastEthernet0/3': None,
         'FastEthernet1/0': None,
         'FastEthernet1/1': None,
         'FastEthernet1/2': None,
         'FastEthernet1/3': None,
         'Vlan100': None},
 'sw2': {'FastEthernet0/0': None,
         'FastEthernet0/1': None,
         'FastEthernet0/2': None,
         'FastEthernet0/3': None,
         'FastEthernet1/0': None,
         'FastEthernet1/1': None,
         'FastEthernet1/2': None,
         'FastEthernet1/3': None,
         'FastEthernet2/0': None,
         'FastEthernet2/1': None,
         'Vlan100': None}}

"""

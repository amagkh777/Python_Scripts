from pprint import pprint

ip_dict = {}

with open("files/sh_ip_int_br.txt") as f:
    for line in f:
        columns = line.split()
        print(columns)
        try:
            intf = columns[0]
            if intf[-1].isdigit():
                ip = columns[1]
                ip_dict[intf] = ip
        except IndexError:
            pass


pprint(ip_dict)

"""
Example:
['R1#show', 'ip', 'interface', 'brief']
[]
['Interface', 'IP-Address', 'OK?', 'Method', 'Status', 'Protocol']
['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up']
['FastEthernet0/1', '10.0.12.1', 'YES', 'manual', 'up', 'up']
['FastEthernet0/2', '10.0.13.1', 'YES', 'manual', 'up', 'up']
['FastEthernet0/3', 'unassigned', 'YES', 'unset', 'up', 'down']
['Loopback0', '10.1.1.1', 'YES', 'manual', 'up', 'up']
['Loopback100', '100.0.0.1', 'YES', 'manual', 'up', 'up']
{'FastEthernet0/0': '15.0.15.1',
 'FastEthernet0/1': '10.0.12.1',
 'FastEthernet0/2': '10.0.13.1',
 'FastEthernet0/3': 'unassigned',
 'Loopback0': '10.1.1.1',
 'Loopback100': '100.0.0.1'}

"""
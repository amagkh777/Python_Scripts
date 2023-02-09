from tabulate import tabulate
from pprint import pprint
import re

"""
R1#show ip interface brief
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            15.0.15.1       YES manual up                    up
FastEthernet0/1            10.0.12.1       YES manual up                    up
FastEthernet0/2            10.0.13.1       YES manual up                    up
FastEthernet0/3            unassigned      YES unset  administratively down down
Loopback0                  10.1.1.1        YES manual up                    up
Loopback100                100.0.0.1       YES manual up                    up
"""
#1 вариант
result = []
regex = (
    r"(\S+) +([\d.]+) +" # interface and IP
    r"\w+ +\w+ +" # trash
    r"(up|down) +(up|down)" # status, protocol
)
with open("sh_ip_int_br.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            result.append(match.groups())

pprint(result)

#2 вариант
result = {}
regex = (
    r"^(\S+) +([\d.]+) +" # interface and IP
)
with open("sh_ip_int_br.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            intf, ip = match.group(1, 2)
            result[intf] = ip

pprint(result)

"""
Example:

#1
[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]
#2
{'FastEthernet0/0': '15.0.15.1',
 'FastEthernet0/1': '10.0.12.1',
 'FastEthernet0/2': '10.0.13.1',
 'Loopback0': '10.1.1.1',
 'Loopback100': '100.0.0.1'}
 
 """
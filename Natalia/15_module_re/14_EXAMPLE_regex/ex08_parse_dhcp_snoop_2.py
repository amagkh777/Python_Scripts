import re
from pprint import pprint

"""
MacAddress         IpAddress  Lease  Type           VLAN  Interface
-----------------  ---------- -----  -------------  ----  -----------------
  10.1.10.2  86250  dhcp-snooping   10    FastEthernet0/1
00:04:A3:3E:5B:69  10.1.5.2   63951  dhcp-snooping   5     FastEthernet0/10
00:05:B3:7E:9B:60  10.1.5.4   63253  dhcp-snooping   5     FastEthernet0/9
00:09:BC:3F:A6:50  10.1.10.6  76260  dhcp-snooping   10    FastEthernet0/3
Total number of bindings: 4
"""

regex = (
    r"(?P<mac>\S+) +"  # мак адрес
    r"(?P<ip>\S+) +"  # ip адрес
    r"\d+ +\S+ +"  # lease, type
    r"(?P<vlan>\d+) +"  # vlan
    r"(?P<intf>\S+)"  # interface
)

result = []

with open("dhcp_snooping.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            result.append(match.group("intf", "vlan", "ip", "mac"))

pprint(result)

"""
Example:

[('FastEthernet0/10', '5', '10.1.5.2', '00:04:A3:3E:5B:69'),
 ('FastEthernet0/9', '5', '10.1.5.4', '00:05:B3:7E:9B:60'),
 ('FastEthernet0/3', '10', '10.1.10.6', '00:09:BC:3F:A6:50')]
 
 """
import re
from pprint import pprint
"""
SW1#show cdp neighbors detail
-------------------------
Device ID: SW2
Entry address(es):
  IP address: 10.1.1.2
Platform: cisco WS-C2960-8TC-L,  Capabilities: Switch IGMP
Interface: GigabitEthernet1/0/16,  Port ID (outgoing port): GigabitEthernet0/1
Holdtime : 164 sec

Version :
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1), Cisco IOS Software
Technical Support: http://www.cisco.com/techsupport

-------------------------
Device ID: R1
Entry address(es):
  IP address: 10.1.1.1
Platform: Cisco 3825,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/22,  Port ID (outgoing port): GigabitEthernet0/0
Holdtime : 156 sec

Version :
Cisco IOS Software, 3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2009 by Cisco Systems, Inc.
-------------------------
Device ID: R2
Entry address(es):
  IP address: 10.2.2.2
Platform: Cisco 2911,  Capabilities: Router Switch IGMP
Interface: GigabitEthernet1/0/21,  Port ID (outgoing port): GigabitEthernet0/0
Holdtime : 156 sec

Version :
Cisco IOS Software, 2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport

"""


regex = (
    r"Device ID: (?P<device>\S+)"
    r"|IP address: (?P<ip>\S+)"
    r"|Platform: (?P<platform>.+?),"
    r"|Cisco IOS Software, (?P<ios>.+),"
    r"|Duplex: (?P<duplex>\S+)"
    r"|Interface: (?P<local_port>\S+), .+: (?P<remote_port>\S+)"
)

result = {}

with open("files/sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            group = match.lastgroup
            value = match.group(group)
            if group == "device":
                result[value] = {}
                device = value
            # elif group == "remote_port":
            #     result[device][group] = value
            #     result[device]["local_port"] = match.group("local_port")
            else:
                result[device][group] = value
            # elif group == "ip":
            #     result[device]["ip"] = value
            # elif group == "platform":
            #     result[device]["platform"] = value
            # elif group == "ios":
            #     result[device]["ios"] = value

pprint(result)

"""
Example:

{'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
           'ip': '10.1.1.1',
           'platform': 'Cisco 3825'},
    'R2': {'ios': '2900 Software (C2911-ADVENTERPRISEK9-M), Version 15.2(2)T1',
           'ip': '10.2.2.2',
           'platform': 'Cisco 2911'},
    'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9',
            'ip': '10.1.1.2',
            'platform': 'cisco WS-C2960-8TC-L'}}
"""
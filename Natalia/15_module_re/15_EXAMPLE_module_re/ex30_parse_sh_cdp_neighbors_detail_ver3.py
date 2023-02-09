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

cdp = {}

regex = (
    r"Device ID: (?P<device>\S+)" # имя устройства
    r"|IP address: (?P<ip>\S+)"
    r"|Platform: (?P<platform>.+),"
    r"|Interface: (?P<port1>\S+), +Port ID \(outgoing port\): (?P<port2>\S+)"
    r"|Cisco IOS Software, (?P<ios>.+),"
)

with open('sh_cdp_neighbors_sw1.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            last = match.lastgroup
            value = match.group(last)
            print(f"Lastgroup = {last:10}, {value}")
            if last == "device":
                device = value
                cdp[device] = {}
            elif last == "port2":
                cdp[device]["port1"] = match.group("port1")
                cdp[device][last] = value
            else:
                cdp[device][last] = value


pprint(cdp)

"""
Example:

Lastgroup = device    , SW2
Lastgroup = ip        , 10.1.1.2
Lastgroup = platform  , cisco WS-C2960-8TC-L
Lastgroup = port2     , GigabitEthernet0/1
Lastgroup = ios       , C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, RELEASE SOFTWARE (fc1)
Lastgroup = device    , R1
Lastgroup = ip        , 10.1.1.1
Lastgroup = platform  , Cisco 3825
Lastgroup = port2     , GigabitEthernet0/0
Lastgroup = ios       , 3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1
Lastgroup = device    , R2
Lastgroup = ip        , 10.2.2.2
Lastgroup = platform  , Cisco 2911
Lastgroup = port2     , GigabitEthernet0/0
Lastgroup = ios       , 2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1
{'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
        'ip': '10.1.1.1',
        'platform': 'Cisco 3825',
        'port1': 'GigabitEthernet1/0/22',
        'port2': 'GigabitEthernet0/0'},
 'R2': {'ios': '2900 Software (C3825-ADVENTERPRISEK9-M), Version 15.2(2)T1',
        'ip': '10.2.2.2',
        'platform': 'Cisco 2911',
        'port1': 'GigabitEthernet1/0/21',
        'port2': 'GigabitEthernet0/0'},
 'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9, '
                'RELEASE SOFTWARE (fc1)',
         'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L',
         'port1': 'GigabitEthernet1/0/16',
         'port2': 'GigabitEthernet0/1'}}

Process finished with exit code 0

"""

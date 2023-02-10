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
#1 вариант 
result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        if line.startswith("Device ID"):
            device = line.split()[-1]
            result[device] = {}
        elif "IP address" in line:
            ip = line.split()[-1]
            result[device]["ip"] = ip
        elif line.startswith("Platform"):
            regex = r"Platform: (.+?),"
            platform = re.search(regex, line).group(1)
            result[device]["platform"] = platform
        elif line.startswith("Cisco IOS Software"):
            regex = r", +Version +(.+?),"
            ios = re.search(regex, line).group(1)
            result[device]["ios"] = ios
        elif line.startswith("Interface"):
            regex = r": (\S+), +.+: (\S+)"
            m = re.search(regex, line)
            result[device]["port1"] = m.group(1)
            result[device]["port2"] = m.group(2)

pprint(result, width=120)


{"SW2": {"ios": "12.2(55)SE9",
         "ip": "10.1.1.2",
         "platform": "cisco WS-C2960-8TC-L"
        }}

#2 вариант
result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        if line.startswith("Device ID"):
            device = line.split()[-1]
        elif "IP address" in line:
            ip = line.split()[-1]
        elif line.startswith("Platform"):
            regex = r"Platform: (.+?),"
            platform = re.search(regex, line).group(1)
        elif line.startswith("Cisco IOS Software"):
            regex = r", +Version +(.+?),"
            ios = re.search(regex, line).group(1)
            result[device] = {"ios": ios, "ip": ip, "platform": platform}

pprint(result, width=120)

"""
Example:

#1
{'R1': {'ios': '12.4(24)T1',
        'ip': '10.1.1.1',
        'platform': 'Cisco 3825',
        'port1': 'GigabitEthernet1/0/22',
        'port2': 'GigabitEthernet0/0'},
 'R2': {'ios': '15.2(2)T1',
        'ip': '10.2.2.2',
        'platform': 'Cisco 2911',
        'port1': 'GigabitEthernet1/0/21',
        'port2': 'GigabitEthernet0/0'},
 'SW2': {'ios': '12.2(55)SE9',
         'ip': '10.1.1.2',
         'platform': 'cisco WS-C2960-8TC-L',
         'port1': 'GigabitEthernet1/0/16',
         'port2': 'GigabitEthernet0/1'}}


#2
{'R1': {'ios': '12.4(24)T1', 'ip': '10.1.1.1', 'platform': 'Cisco 3825'},
 'R2': {'ios': '15.2(2)T1', 'ip': '10.2.2.2', 'platform': 'Cisco 2911'},
 'SW2': {'ios': '12.2(55)SE9', 'ip': '10.1.1.2', 'platform': 'cisco WS-C2960-8TC-L'}}

"""
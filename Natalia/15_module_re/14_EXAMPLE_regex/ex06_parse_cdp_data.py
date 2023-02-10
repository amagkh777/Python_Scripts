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

result = {}

with open("sh_cdp_neighbors_sw1.txt") as f:
    for line in f:
        if line.startswith("Device ID"):
            device = line.split()[-1]
        elif line.startswith("Interface"):
            m = re.search(r"Port ID \(outgoing port\): (\S+)", line)
            r_intf = m.group(1)
        elif line.startswith("Cisco IOS Software"):
            regex = r", +Version +(.+?),"
            ios = re.search(regex, line).group(1)
            result[device] = (ios, r_intf)

pprint(result)

"""
Example:

{'R1': ('12.4(24)T1', 'GigabitEthernet0/0'),
 'R2': ('15.2(2)T1', 'GigabitEthernet0/0'),
 'SW2': ('12.2(55)SE9', 'GigabitEthernet0/1')}

"""
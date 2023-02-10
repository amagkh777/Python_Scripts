from pprint import pprint
import re
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

def parse_cdp_file(filename):
    regex = (
        r"^Device ID: (?P<hostname>\S+)"
        r".+?"
        r" +IP address: (?P<ip>\S+)\n"
        r"^Platform: (?P<platform>.+?), .+?"
        r"^Interface: (?P<local_port>\S+), .+?: (?P<remote_port>\S+)"
        r".+?"
        r"^Cisco IOS Software, (?P<ios>.+?), RELEASE"
        r".+?"
        r"^advertisement version: (?P<vtp_version>\d+)"
    )
    result_dict = {}
    with open(filename) as f:
        match_all = re.finditer(regex, f.read(), re.DOTALL|re.MULTILINE)
        for match in match_all:
            n_dict = match.groupdict()
            hostname = n_dict.pop("hostname")
            result_dict[hostname] = n_dict
    return result_dict




if __name__ == "__main__":
    result = parse_cdp_file("sh_cdp_neighbors_sw1.txt")
    pprint(result)
    
"""
Example:

{'R1': {'ios': '3800 Software (C3825-ADVENTERPRISEK9-M), Version 12.4(24)T1',
        'ip': '10.1.1.1',
        'local_port': 'GigabitEthernet1/0/22',
        'platform': 'Cisco 3825',
        'remote_port': 'GigabitEthernet0/0',
        'vtp_version': '2'},
 'R2': {'ios': '2900 Software (C2911-ADVENTERPRISEK9-M), Version 15.2(2)T1',
        'ip': '10.2.2.2',
        'local_port': 'GigabitEthernet1/0/21',
        'platform': 'Cisco 2911',
        'remote_port': 'GigabitEthernet0/0',
        'vtp_version': '2'},
 'SW2': {'ios': 'C2960 Software (C2960-LANBASEK9-M), Version 12.2(55)SE9',
         'ip': '10.1.1.2',
         'local_port': 'GigabitEthernet1/0/16',
         'platform': 'cisco WS-C2960-8TC-L',
         'remote_port': 'GigabitEthernet0/1',
         'vtp_version': '2'}}

"""


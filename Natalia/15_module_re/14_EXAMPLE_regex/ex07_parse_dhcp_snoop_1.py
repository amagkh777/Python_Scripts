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


def parse_dhcp_snooping(filename):
    result = []
    regex = (
        r"(?P<mac>\S+) +(?P<ip>\S+) +"
        r"\d+ +\S+ +"
        r"(?P<vlan>\d+) +(?P<intf>\S+)"
    )
    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                result.append(match.groupdict())
    return result


if __name__ == "__main__":
    output = parse_dhcp_snooping("dhcp_snooping.txt")
    pprint(output)
    for data_dict in output:
        print(data_dict["ip"])

"""
Example:

[{'intf': 'FastEthernet0/10',
  'ip': '10.1.5.2',
  'mac': '00:04:A3:3E:5B:69',
  'vlan': '5'},
 {'intf': 'FastEthernet0/9',
  'ip': '10.1.5.4',
  'mac': '00:05:B3:7E:9B:60',
  'vlan': '5'},
 {'intf': 'FastEthernet0/3',
  'ip': '10.1.10.6',
  'mac': '00:09:BC:3F:A6:50',
  'vlan': '10'}]
10.1.5.2
10.1.5.4
10.1.10.6

"""


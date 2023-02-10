from pprint import pprint
import re
"""
log.txt

%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/19
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/16
"""
regex = r"Host (\S+) .+ port (\S+) and port (\S+)"

ports = set()

with open("files/log.txt") as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            # print(match.groups())
            # print(match.group(2, 3))
            ports.update(match.group(2, 3))
print(ports)

"""
Example:

 {'Gi0/16', 'Gi0/24', 'Gi0/19'}

"""

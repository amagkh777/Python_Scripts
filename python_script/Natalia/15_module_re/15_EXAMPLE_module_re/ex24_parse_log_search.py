import re
"""
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/19
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/16

test kajsdfksaj
"""
regex = (r"vlan (?P<vlan>\d+) is flapping between "
         r"port (?P<port1>\S+) and port (?P<port2>\S+)")


ports = set()

with open('log.txt') as f:
    for line in f:
        match = re.search(regex, line)
        if match:
            vlan, port1, port2 = match.groups()
            ports.update({port1, port2})

print("Петля между портами {} в VLAN {}".format(", ".join(ports), vlan))

"""
Example:

Петля между портами Gi0/19, Gi0/24, Gi0/16 в VLAN 10

"""
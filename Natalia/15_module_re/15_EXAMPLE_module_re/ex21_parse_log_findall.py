import re
"""
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/19
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/16

test kajsdfksaj
"""

regex = "Host \S+ " "in vlan (\d+) " "is flapping between port " "(\S+) and port (\S+)"

ports = set()

with open("log.txt") as f:
    result = re.findall(regex, f.read())
    for vlan, port1, port2 in result:
        ports.add(port1)
        ports.add(port2)

print("Петля между портами {} в VLAN {}".format(", ".join(ports), vlan))


"""
Example:

Петля между портами Gi0/16, Gi0/19, Gi0/24 в VLAN 10

"""
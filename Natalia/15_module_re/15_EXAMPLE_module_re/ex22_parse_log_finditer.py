import re
"""
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/19
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/16

test kajsdfksaj
"""
regex = (
    r"Host (\S+) "
    r"in vlan (\d+) .+"
    r"port (\S+) and port (\S+)"
)

ports = set()

with open("log.txt") as f:
    all_match = re.finditer(regex, f.read())
    for m in all_match:
        host, vlan, port1, port2 = m.groups()
        ports.update((port1, port2))

print(ports)

"""
Example:

{'Gi0/19', 'Gi0/24', 'Gi0/16'}

"""
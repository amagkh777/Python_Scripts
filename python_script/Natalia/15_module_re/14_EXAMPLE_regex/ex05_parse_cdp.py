import re
from pprint import pprint
"""

SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID    Local Intrfce   Holdtme     Capability    Platform    Port ID
R1           Eth 0/1         122           R S I        2811       Eth 0/0
R2           Eth 0/2         143           R S I        2811       Eth 0/0
R3           Eth 0/3         151           R S I        2811       Eth 0/0
R6           Eth 0/5         121           R S I        2811       Eth 0/1
R15.Cisco.ComEth 0/6         121           R S I        2811       Eth 0/15

"""


def parse_cdp(filename):
    result = []
    regex = (
        r"^(\S+) +(\S+ [\d/]+) +\d+.+ +(\S+ [\d/]+)$"
    )
    with open(filename) as f:
        for line in f:
            match_host = re.search(r"^(\S+)[>#]", line)
            match_n = re.search(regex, line)
            if match_host:
                hostname = match_host.group(1)
            elif match_n:
                #result.append((hostname, *match_n.group(2, 1, 3)))
                l_intf, remote_d, remote_int = match_n.group(2, 1, 3)
                result.append((hostname, l_intf, remote_d, remote_int))
    return result


if __name__ == "__main__":
    output = parse_cdp("sh_cdp_n_sw1.txt")
    pprint(output)

"""
Example:

[('SW1', 'Eth 0/1', 'R1', 'Eth 0/0'),
 ('SW1', 'Eth 0/2', 'R2', 'Eth 0/0'),
 ('SW1', 'Eth 0/3', 'R3', 'Eth 0/0'),
 ('SW1', 'Eth 0/5', 'R6', 'Eth 0/1')]

"""
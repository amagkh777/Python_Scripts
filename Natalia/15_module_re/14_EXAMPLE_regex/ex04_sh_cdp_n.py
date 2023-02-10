from pprint import pprint
import re
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

regex = r"^(\S+) *([A-Z]\S+ \S+) +\d+ .+ (\S+ \S+)$"

with open("sh_cdp_n_sw1.txt") as f:
    for line in f:
        m = re.search(regex, line)
        if m:
            print(m.groups())
            
"""
Example:

('R1', 'Eth 0/1', 'Eth 0/0')
('R2', 'Eth 0/2', 'Eth 0/0')
('R3', 'Eth 0/3', 'Eth 0/0')
('R6', 'Eth 0/5', 'Eth 0/1')
('R15.Cisco.Com', 'Eth 0/6', 'Eth 0/15')

"""
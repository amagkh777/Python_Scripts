import re
from pprint import pprint
"""
R1#show ip interface brief
Interface                  IP-Address      OK? Method Status      Protocol
FastEthernet0/0            15.0.15.1       YES manual up          up
FastEthernet0/1            10.0.12.1       YES manual up          up
FastEthernet0/2            10.0.13.1       YES manual up          up
FastEthernet0/3            unassigned      YES unset  up          up
Loopback0                  10.1.1.1        YES manual up          up
Loopback100                100.0.0.1       YES manual up          up
"""

def parse_sh_ip_int_br(output):
    regex = r"^(\S+) +([\d.]+|unassigned)"

    result_dict = {}

    for line in output.split("\n"):
        m = re.search(regex, line)
        if m:
            intf = m.group(1)
            ip = m.group(2)
            if ip == "unassigned":
                ip = None
            result_dict[intf] = ip
    return result_dict


if __name__ == "__main__":
    with open("sh_ip_int_br.txt", "r") as f:
        content = f.read()
    pprint(parse_sh_ip_int_br(content))

"""
Example:

{'FastEthernet0/0': '15.0.15.1',
 'FastEthernet0/1': '10.0.12.1',
 'FastEthernet0/2': '10.0.13.1',
 'FastEthernet0/3': None,
 'Loopback0': '10.1.1.1',
 'Loopback100': '100.0.0.1'}
 
 """
from pprint import pprint
import re
"""
R1#show ip interface brief
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            15.0.15.1       YES manual up                    up
FastEthernet0/1            10.0.12.1       YES manual up                    up
FastEthernet0/2            10.0.13.1       YES manual up                    up
FastEthernet0/3            unassigned      YES unset  administratively down down
Loopback0                  10.1.1.1        YES manual up                    up
Loopback100                100.0.0.1       YES manual up                    up

"""

def parse_sh_ip_int_br(output):
    regex = r"(\S+) +(\S+) +\w+ +\w+ +(up|down) +(up|down)"
    all_match = re.finditer(regex, output)
    # for match in all_match:
    #    print(match.groups())

    results = [match.groups() for match in all_match]
    return results


if __name__ == "__main__":
    with open("files/sh_ip_int_br.txt", "r") as f:
        content = f.read()
    pprint(parse_sh_ip_int_br(content))

"""
Example:

[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('unassigned', 'YES', 'down', 'down'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]
 
 """
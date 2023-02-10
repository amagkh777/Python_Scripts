from pprint import pprint
import re


def parse_cdp_file(filename):
    regex = re.compile(
        r"Device ID: (?P<hostname>.+)\n"
        r".+\n"
        r" +IP address: (?P<ip>\S+)\n"
        r"Platform: (?P<platform>.+?), .+\n"
        r"Interface: (?P<local_port>\S+), .+: (?P<remote_port>\S+)\n"
        r"(.*\n)+?"
        r"Cisco IOS Software, (?P<ios>.+), RELEASE .+\n"
        r"(.*\n)+?"
        r"advertisement version: (?P<vtp_version>\d+)"
    )
    result_dict = {}
    with open(filename) as f:
        match_all = regex.finditer(f.read())
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
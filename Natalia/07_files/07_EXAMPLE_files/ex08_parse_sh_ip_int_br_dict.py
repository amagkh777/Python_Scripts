from pprint import pprint

result_dict = {}

with open("sh_ip_int_br.txt", "r") as f:
    for line in f:
        line_list = line.split()
        if line_list and line_list[0][-1].isdigit():
            intf = line_list[0]
            ip = line_list[1]
            if ip == "unassigned":
                ip = None
            result_dict[intf] = ip

pprint(result_dict)

# Просмотр данных
for intf, ip in result_dict.items():
    if not ip:
        print(intf)

"""
Example:

{'FastEthernet0/0': '15.0.15.1',
 'FastEthernet0/1': '10.0.12.1',
 'FastEthernet0/2': '10.0.13.1',
 'FastEthernet0/3': None,
 'Loopback0': '10.1.1.1',
 'Loopback100': '100.0.0.1'}
FastEthernet0/3

"""
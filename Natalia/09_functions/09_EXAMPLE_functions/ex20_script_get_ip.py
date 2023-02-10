from pprint import pprint


def get_intf_ip_dict_from_cfg(filename):
    intf_ip_dict = {}
    with open(filename) as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
            elif line.startswith(" ip address"):
                ip = line.split()[-2]
                intf_ip_dict[intf] = ip

    return intf_ip_dict


r1 = get_intf_ip_dict_from_cfg("config_r1.txt")
pprint(r1)
r2 = get_intf_ip_dict_from_cfg("config_r2.txt")
pprint(r2)

config_list = ["config_r1.txt", "config_r2.txt", "config_r3.txt", "config_sw1.txt"]
for cfg in config_list:
    result = get_intf_ip_dict_from_cfg(cfg)
    pprint(result)

"""
Example:

{'Ethernet0/0': '10.0.13.1',
 'Ethernet0/2': '10.0.19.1',
 'Loopback0': '10.1.1.1'}
{'Ethernet0/0': '10.0.23.2',
 'Ethernet0/1': '10.255.2.2',
 'Ethernet0/2': '10.0.29.2',
 'Loopback0': '10.2.2.2'}
{'Ethernet0/0': '10.0.13.1',
 'Ethernet0/2': '10.0.19.1',
 'Loopback0': '10.1.1.1'}
{'Ethernet0/0': '10.0.23.2',
 'Ethernet0/1': '10.255.2.2',
 'Ethernet0/2': '10.0.29.2',
 'Loopback0': '10.2.2.2'}
{'Ethernet0/0': '10.0.13.3', 'Loopback0': '10.3.3.3'}
{'Vlan100': '10.0.100.1'}

"""
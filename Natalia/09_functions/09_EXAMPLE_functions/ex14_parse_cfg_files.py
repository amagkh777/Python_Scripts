from pprint  import pprint



def get_intf_ip_from_cfg(filename):
    output = {}
    with open(filename) as f:
        for line in f:
            words = line.split()
            if line.startswith("interface"):
                interface = words[-1]
            elif line.startswith(" ip address"):
                ip = words[-2]
                output[interface] = ip
    return output


files = ["config_r1.txt", "config_sw1.txt", "config_sw2.txt"]

all_data = {}

for file in files:
    host = file.split(".")[0].split("_")[-1]
    result = get_intf_ip_from_cfg(file)
    pprint(result)
    all_data[host] = result

print("####################")
pprint(all_data)

"""
Example:

{'Ethernet0/0': '10.0.13.1',
 'Ethernet0/2': '10.0.19.1',
 'Loopback0': '10.1.1.1'}
{'Vlan100': '10.0.100.1'}
{'Vlan100': '10.0.100.2'}
####################
{'r1': {'Ethernet0/0': '10.0.13.1',
        'Ethernet0/2': '10.0.19.1',
        'Loopback0': '10.1.1.1'},
 'sw1': {'Vlan100': '10.0.100.1'},
 'sw2': {'Vlan100': '10.0.100.2'}}

"""
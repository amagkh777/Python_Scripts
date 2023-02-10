from pprint import pprint
with open("sh_ip_int_br.txt") as f:
    result = []
    for line in f:
        line_list = line.split()
        if line_list:
            intf, ip, *_, st, prot = line_list
            result.append([intf, ip, st, prot])

pprint(result)


"""
Example:

[['R1#show', 'ip', 'interface', 'brief'],
 ['Interface', 'IP-Address', 'Status', 'Protocol'],
 ['FastEthernet0/0', '15.0.15.1', 'up', 'up'],
 ['FastEthernet0/1', '10.0.12.1', 'up', 'up'],
 ['FastEthernet0/2', '10.0.13.1', 'up', 'up'],
 ['FastEthernet0/3', 'unassigned', 'up', 'down'],
 ['Loopback0', '10.1.1.1', 'up', 'up'],
 ['Loopback100', '100.0.0.1', 'up', 'up']]

"""
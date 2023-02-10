result = {}

with open("sh_ip_int_br.txt") as f:
    for line in f:
        line_list = line.split()
        # print(line_list)
        # ['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up']
        # line_list[1] = '15.0.15.1'
        # line_list[1][0] = '1'
        if len(line_list) > 2 and line_list[1][0].isdigit():
            print(line_list)
            intf = line_list[0]
            ip = line_list[1]
            result[intf] = ip

print(result)


"""
Example:

['FastEthernet0/0', '15.0.15.1', 'YES', 'manual', 'up', 'up']
['FastEthernet0/1', '10.0.12.1', 'YES', 'manual', 'up', 'up']
['FastEthernet0/2', '10.0.13.1', 'YES', 'manual', 'up', 'up']
['Loopback0', '10.1.1.1', 'YES', 'manual', 'up', 'up']
['Loopback100', '100.0.0.1', 'YES', 'manual', 'up', 'up']
{'FastEthernet0/0': '15.0.15.1', 'FastEthernet0/1': '10.0.12.1', 'FastEthernet0/2': '10.0.13.1', 'Loopback0': '10.1.1.1', 'Loopback100': '100.0.0.1'}

"""

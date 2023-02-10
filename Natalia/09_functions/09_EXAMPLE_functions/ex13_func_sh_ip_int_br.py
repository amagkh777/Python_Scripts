from pprint import pprint


def get_intf_ip_dict(filename):
    """
    Функция ожидает имя файла с выводом sh ip int br.
    Возвращает словарь intf: ip
    """
    result = {}

    with open(filename) as f:
        for line in f:
            line_list = line.split()
            if len(line_list) > 2 and line_list[1][0].isdigit():
                intf = line_list[0]
                ip = line_list[1]
                result[intf] = ip

    return result


files = ["sh_ip_int_br.txt", "sh_ip_int_br2.txt"]

for file in files:
    data = get_intf_ip_dict(file)
    pprint(data)



"""
Example:

{'FastEthernet0/0': '15.0.15.1',
 'FastEthernet0/1': '10.0.12.1',
 'FastEthernet0/2': '10.0.13.1',
 'Loopback0': '10.1.1.1',
 'Loopback100': '100.0.0.1'}
{'Ethernet0/0': '192.168.100.1',
 'Ethernet0/1': '192.168.200.1',
 'Ethernet0/3': '192.168.130.1',
 'Loopback100': '10.1.1.100',
 'Loopback123': '123.1.2.3',
 'Loopback22': '10.2.2.2',
 'Loopback55': '5.5.5.5'}

"""



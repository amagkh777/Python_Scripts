from filter_functions import filter_file_lines
from pprint import pprint

pprint(filter_file_lines("config_r1.txt", "interface"))

"""
Example:

['interface Loopback0\n',
 'interface Tunnel0\n',
 'interface Ethernet0/0\n',
 'interface Ethernet0/1\n',
 'interface Ethernet0/2\n',
 'interface Ethernet0/3\n',
 'interface Ethernet0/3.100\n',
 'interface Ethernet1/0\n',
 ' event neighbor-discovery interface regexp .*Ethernet.* cdp add\n',
 ' action 3.0 cli command "interface $_nd_local_intf_name"\n']

"""
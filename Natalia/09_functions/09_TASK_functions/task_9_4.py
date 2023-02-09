

ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):

    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status


def convert_config_to_dict(config_filename):
    config_dict = {}
    with open(config_filename) as f:
        for line in f:
            line = line.rstrip()
            if line and not (line.startswith("!") or ignore_command(line, ignore)):
                if line[0].isalnum():
                    section = line
                    config_dict[section] = []
                else:
                    config_dict[section].append(line.strip())
    return config_dict


pprint(convert_config_to_dict("config_sw1.txt"))


"""
Example:

{'end': [],
 'hostname sw1': [],
 'interface FastEthernet0/0': ['switchport mode access',
                               'switchport access vlan 10'],
 'interface FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 100,200',
                               'switchport mode trunk'],
 'interface FastEthernet0/2': ['switchport mode access',
                               'switchport access vlan 20'],
 'interface FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan '
                               '100,300,400,500,600',
                               'switchport mode trunk'],
 'interface FastEthernet1/0': ['switchport mode access',
                               'switchport access vlan 20'],
 'interface FastEthernet1/1': ['switchport mode access',
                               'switchport access vlan 30'],
 'interface FastEthernet1/2': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 400,500,600',
                               'switchport mode trunk'],
 'interface FastEthernet1/3': [],
 'interface Vlan100': ['ip address 10.0.100.1 255.255.255.0'],
 'line aux 0': [],
 'line con 0': ['exec-timeout 0 0',
                'privilege level 15',
                'logging synchronous'],
 'line vty 0 4': ['login', 'transport input all'],
 'no service password-encryption': [],
 'service timestamps debug datetime msec': [],
 'service timestamps log datetime msec': [],
 'version 15.0': []}

Process finished with exit code 0


"""
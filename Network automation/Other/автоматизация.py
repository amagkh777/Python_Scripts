#1
# COMMANDS = {
#  'description': 'description {}',
#  'speed': 'speed {}',
#  'duplex': 'duplex {}',
#  }
# CONFIG_PARAMS = {
#  'description': 'auto description by Python',
#  'speed': '10000',
#  'duplex': 'auto'
#  }
#
# commands_list = []
#
# for feature, value in CONFIG_PARAMS.items():
#     command = COMMANDS.get(feature).format(value)
#     commands_list.append(command)
# print(commands_list)

#2________________________________________________________
# vendors = ['arista', 'juniper', 'big_switch', 'cisco']
#
# for index, each in enumerate(vendors):
#     print(str(index) + ' ' + each)


#3________________________________________________________
def get_commands(vlan, name):
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)
    return commands

def push_commands(device, commands):
    print('Connecting to device: ' + device)
    for cmd in commands:
        print('Sending command: ' + cmd)


devices = ['switch1', 'switch2', 'switch3']
vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'},
{'id': '30', 'name': 'WLAN'}]

for vlan in vlans:
    id = vlan.get('id')
    name = vlan.get('name')
    print('\n')
    print('CONFIGURING VLAN:' + id)
    commands = get_commands(id, name)
    for device in devices:
        push_commands(device, commands)
        print('\n')

#4________________________________________________________
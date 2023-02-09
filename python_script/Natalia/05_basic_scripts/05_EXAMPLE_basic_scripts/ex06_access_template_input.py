interface = input("Enter interface type and number: ")
vlan = input("Enter VLAN number: ")

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

print("\n" + "-" * 30)
print("interface {}".format(interface))
print("\n".join(access_template).format(vlan))


"""
Example:

Enter interface type and number: fa1/1
Enter VLAN number: 23

------------------------------
interface fa1/1
switchport mode access
switchport access vlan 23
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

"""
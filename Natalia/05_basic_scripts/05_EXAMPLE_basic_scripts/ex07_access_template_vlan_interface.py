# -*- coding: utf-8 -*-
access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]


template = {"access": access_template, "trunk": trunk_template}

mode = input("Введите режим работы интерфейса (access/trunk): ")
interface = input("Введите тип и номер интерфейса: ")
vlans = input("Введите номер влан(ов): ")

print(f"interface {interface}")
print("\n".join(template[mode]).format(vlans))


"""
Example:

Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса: fa1/1
Введите номер влан(ов): 2,4,5
interface fa1/1
switchport mode access
switchport access vlan 2,4,5
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

"""
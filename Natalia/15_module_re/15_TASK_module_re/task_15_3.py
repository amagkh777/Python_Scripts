# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re


def convert_ios_nat_to_asa(cisco_ios, cisco_asa):
    regex = (
        "tcp (?P<local_ip>\S+) +(?P<lport>\d+) +interface +\S+ (?P<outside_port>\d+)"
    )
    asa_template = (
        "object network LOCAL_{local_ip}\n"
        " host {local_ip}\n"
        " nat (inside,outside) static interface service tcp {lport} {outside_port}\n"
    )
    with open(cisco_ios) as f, open(cisco_asa, "w") as asa_nat_cfg:
        data = re.finditer(regex, f.read())
        for match in data:
            asa_nat_cfg.write(asa_template.format(**match.groupdict()))


if __name__ == "__main__":
    convert_ios_nat_to_asa("cisco_nat_config.txt", "cisco_asa_config.txt")
    
    
"""
Exqmple:

object network LOCAL_10.66.0.13
 host 10.66.0.13
 nat (inside,outside) static interface service tcp 995 995
object network LOCAL_10.66.0.21
 host 10.66.0.21
 nat (inside,outside) static interface service tcp 20065 20065
object network LOCAL_10.66.0.22
 host 10.66.0.22
 nat (inside,outside) static interface service tcp 443 44443
object network LOCAL_10.66.0.23
 host 10.66.0.23
 nat (inside,outside) static interface service tcp 2565 2565
object network LOCAL_10.1.2.28
 host 10.1.2.28
 nat (inside,outside) static interface service tcp 563 563
object network LOCAL_10.98.1.1
 host 10.98.1.1
 nat (inside,outside) static interface service tcp 3389 3389
object network LOCAL_10.14.1.15
 host 10.14.1.15
 nat (inside,outside) static interface service tcp 12220 12220
object network LOCAL_10.14.1.169
 host 10.14.1.169
 nat (inside,outside) static interface service tcp 25565 25565
object network LOCAL_10.66.0.26
 host 10.66.0.26
 nat (inside,outside) static interface service tcp 220 220
object network LOCAL_10.66.37.11
 host 10.66.37.11
 nat (inside,outside) static interface service tcp 80 8080
object network LOCAL_10.66.37.13
 host 10.66.37.13
 nat (inside,outside) static interface service tcp 10995 10995
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.2.66
 host 10.1.2.66
 nat (inside,outside) static interface service tcp 22 20023
object network LOCAL_10.1.2.63
 host 10.1.2.63
 nat (inside,outside) static interface service tcp 80 80

"""
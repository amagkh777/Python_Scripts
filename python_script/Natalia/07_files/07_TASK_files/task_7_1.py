# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

output = "\n{:25} {}" * 5

with open("ospf.txt", "r") as f:
    for line in f:
        route = line.replace(",", " ").replace("[", "").replace("]", "")
        route = route.split()

        print(output.format(
                "Prefix", route[1],
                "AD/Metric", route[2],
                "Next-Hop", route[4],
                "Last update", route[5],
                "Outbound Interface", route[6],
        ))

"""

Example:

Prefix                    10.0.24.0/24
AD/Metric                 110/41
Next-Hop                  10.0.13.3
Last update               3d18h
Outbound Interface        FastEthernet0/0

Prefix                    10.0.28.0/24
AD/Metric                 110/31
Next-Hop                  10.0.13.3
Last update               3d20h
Outbound Interface        FastEthernet0/0

Prefix                    10.0.37.0/24
AD/Metric                 110/11
Next-Hop                  10.0.13.3
Last update               3d20h
Outbound Interface        FastEthernet0/0

Prefix                    10.0.41.0/24
AD/Metric                 110/51
Next-Hop                  10.0.13.3
Last update               3d20h
Outbound Interface        FastEthernet0/0

Prefix                    10.0.78.0/24
AD/Metric                 110/21
Next-Hop                  10.0.13.3
Last update               3d20h
Outbound Interface        FastEthernet0/0

Prefix                    10.0.79.0/24
AD/Metric                 110/20
Next-Hop                  10.0.19.9
Last update               4d02h
Outbound Interface        FastEthernet0/2

Process finished with exit code 0


"""
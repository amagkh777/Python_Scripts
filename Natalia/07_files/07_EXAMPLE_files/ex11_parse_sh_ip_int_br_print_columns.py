
with open("sh_ip_int_br.txt") as f:
    for line in f:
        columns = line.split()
        if columns and columns[0][-1].isdigit():
            intf = columns[0]
            ip = columns[1]
            print(f"{intf:20}{ip:15}")

            
"""
Example:

FastEthernet0/0     15.0.15.1      
FastEthernet0/1     10.0.12.1      
FastEthernet0/2     10.0.13.1      
FastEthernet0/3     unassigned     
Loopback0           10.1.1.1       
Loopback100         100.0.0.1 

"""
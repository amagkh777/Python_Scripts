with open("sh_ip_int_br.txt") as src:
    with open("result.txt", "w") as dest:
        for line in src:
            if line.startswith("Fast"):
                dest.write(line)

print()

"""
Example:

FastEthernet0/0       15.0.15.1       YES manual up             up
FastEthernet0/1       10.0.12.1       YES manual up             up
FastEthernet0/2       10.0.13.1       YES manual up             up
FastEthernet0/3       unassigned      YES unset  up             down

"""
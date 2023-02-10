# path = (
#     "/home/vagrant/repos/pyneng-11/"
#     "pyneng-online-11-jun-aug-2021/examples/07_files"
# )
files = ["sh_cdp_n_r1.txt", "sh_cdp_n_r2.txt", "sh_cdp_n_r3.txt", "sh_cdp_n_sw1.txt"]
print(files)

for file in files:
    with open(f"{file}", "r") as f:
        print(f"{file}")
        for line in f:
            if "Eth" in line:
                print(line.rstrip())

                
"""
Example:

['files/sh_cdp_n_r1.txt', 'files/sh_cdp_n_r2.txt', 'files/sh_cdp_n_r3.txt', 'files/sh_cdp_n_sw1.txt']
files/sh_cdp_n_r1.txt
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1
files/sh_cdp_n_r2.txt
SW1              Eth 0/0            125          S I      WS-C3750- Eth 0/2
SW2              Eth 0/1            137          S I      WS-C3750- Eth 0/11
files/sh_cdp_n_r3.txt
SW1              Eth 0/0            131          S I      WS-C3750- Eth 0/3
R4               Eth 0/1            145        R S I      2811      Eth 0/0
R5               Eth 0/2            123        R S I      2811      Eth 0/0
files/sh_cdp_n_sw1.txt
R1           Eth 0/1         122           R S I           2811       Eth 0/0
R2           Eth 0/2         143           R S I           2811       Eth 0/0
R3           Eth 0/3         151           R S I           2811       Eth 0/0
R6           Eth 0/5         121           R S I           2811       Eth 0/1

"""
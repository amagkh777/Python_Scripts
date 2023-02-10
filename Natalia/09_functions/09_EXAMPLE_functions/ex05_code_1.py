with open("config_r1.txt") as f:
    for index, line in enumerate(f, 1):
        print(f"{index:<5}{line}", end="")

        
"""
Example:
1    Current configuration : 4052 bytes
2    !
3    ! Last configuration change at 13:13:40 UTC Tue Mar 1 2016
4    version 15.2
5    no service timestamps debug uptime
6    no service timestamps log uptime
7    no service password-encryption
8    !
9    hostname PE_r1
10   !
11   boot-start-marker
12   boot-end-marker
13   !
14   !
15   logging buffered 50000
16   !
17   no aaa new-model
18   !
19   mmi polling-interval 60
20   no mmi auto-configure
21   no mmi pvc
22   mmi snmp-timeout 180
23   ip auth-proxy max-login-attempts 5
24   ip admission max-login-attempts 5
25   !
26   !
27   !
28   !
29   !
30   no ip domain lookup
31   ip cef
32   no ipv6 cef
33   !
34   multilink bundle-name authenticated
35   mpls label range 1000 1999
36   mpls label protocol ldp
37   mpls ldp explicit-null
38   mpls ldp discovery targeted-hello accept
39   mpls traffic-eng tunnels
40   xconnect logging redundancy
41   !
42   !
43   !
44   !
45   !
46   !
47   !
48   !
49   !
50   interface Loopback0
51    ip address 10.1.1.1 255.255.255.255
52   !
53   interface Tunnel0
54    ip unnumbered Loopback0
55    tunnel mode mpls traffic-eng
56    tunnel destination 10.2.2.2
57    tunnel mpls traffic-eng priority 7 7
58    tunnel mpls traffic-eng bandwidth 5000
59    tunnel mpls traffic-eng path-option 10 dynamic
60    no routing dynamic
61   !
62   interface Ethernet0/0
63    description To PE_r3 Ethernet0/0
64    bandwidth 100000
65    ip address 10.0.13.1 255.255.255.0
66    mpls traffic-eng tunnels
67    ip rsvp bandwidth 100000 10000
68   !
69   interface Ethernet0/1
70    no ip address
71   !
72   interface Ethernet0/2
73    description To P_r9 Ethernet0/2
74    ip address 10.0.19.1 255.255.255.0
75    mpls traffic-eng tunnels
76    ip rsvp bandwidth
77   !
78   interface Ethernet0/3
79    description To sw1 Ethernet0/3
80    no ip address
81   !
82   interface Ethernet0/3.100
83    encapsulation dot1Q 100
84    xconnect 10.2.2.2 12100 encapsulation mpls
85     backup peer 10.4.4.4 14100
86     backup delay 1 1
87   !
88   interface Ethernet1/0
89    no ip address
90    shutdown
91   !
92   router ospf 1
93    mpls ldp autoconfig area 0
94    mpls traffic-eng router-id Loopback0
95    mpls traffic-eng area 0
96    network 10.0.0.0 0.255.255.255 area 0
97   !
98   router bgp 100
99    bgp log-neighbor-changes
100   bgp bestpath igp-metric ignore
101   neighbor 10.2.2.2 remote-as 100
102   neighbor 10.2.2.2 update-source Loopback0
103   neighbor 10.2.2.2 next-hop-self
104   neighbor 10.4.4.4 remote-as 40
105   !
106   address-family vpnv4
107    neighbor 10.2.2.2 activate
108    neighbor 10.2.2.2 send-community both
109    exit-address-family
110  !
111  ip forward-protocol nd
112  !
113  !
114  no ip http server
115  no ip http secure-server
116  ip route 10.2.2.2 255.255.255.255 Tunnel0
117  !
118  ip access-list standard LDP
119   deny   10.0.0.0 0.0.255.255
120   permit 10.0.0.0 0.255.255.255
121  !
122  !
123  ip prefix-list TEST seq 5 permit 10.6.6.6/32
124  !
125  !
126  mpls ldp router-id Loopback0 force
127  !
128  control-plane
129  !
130  !
131  !
132  !
133  alias configure sh do sh
134  alias exec ospf sh run | s ^router ospf
135  alias exec bri show ip int bri | exc unass
136  alias exec id show int desc
137  alias exec top sh proc cpu sorted | excl 0.00%__0.00%__0.00%
138  alias exec c conf t
139  alias exec diff sh archive config differences nvram:startup-config system:running-config
140  alias exec shcr sh run | s ^crypto
141  alias exec desc sh int desc | ex down
142  alias exec bgp sh run | s ^router bgp
143  alias exec xc sh xconnect all
144  alias exec vc sh mpls l2tr vc
145  !
146  line con 0
147   exec-timeout 0 0
148   privilege level 15
149   logging synchronous
150  line aux 0
151  line vty 0 4
152   login
153   transport input all
154  !
155  event manager applet update-int-desc
156   event neighbor-discovery interface regexp .*Ethernet.* cdp add
157   action 1.0 cli command "enable"
158   action 2.0 cli command "config t"
159   action 3.0 cli command "interface $_nd_local_intf_name"
160   action 4.0 cli command "description To $_nd_cdp_entry_name $_nd_port_id"
161   action 5.0 syslog msg "Description for $_nd_local_intf_name changed to $_nd_cdp_entry_name $_nd_port_id"
162   action 6.0 cli command "end"
163   action 7.0 cli command "exit"
164  !
165  end

"""
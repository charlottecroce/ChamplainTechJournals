
# RW01 -> WEB
security issue:  rw01 knows the internal routing for our DMZ and used this information to create a static route from SEC350-WAN to the DMZ.  A better alternative is to mask the presence of the DMZ altogether with NAT destination rules.

- remove static ip route from rw01 to DMZ
```
sudo ip route del 172.16.50.0/29
```

## WAN to DMZ NAT
We've worked with NAT **source** rules when dealing with traffic from inside the network going out to the WAN.  Now we are going to add a NAT **destination** rule (aka port forwarding) so that any port 80 traffic coming to our firewall's WAN/eth0 interface will be forwarded on to web01. 
```
set nat destination rule 10 description "HTTP->WEB01"
set nat destination rule 10 inbound-interface eth0
set nat destination rule 10 destination port 80
set nat destination rule 10 protocol tcp
set nat destination rule 10 translation address 172.16.50.3
```

## Jump server
- log01 is back! but it's a jump server now
- IP Address: 172.16.50.4/29
- hostname: jump-charlotte


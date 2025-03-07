
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


- Adjust the firewall rules from LAN-TO-DMZ  such that mgmt01 can ssh into any server on the DMZ.


- Make sure that fw01 is only listening for SSH on the LAN interface (172.16.150.2) and not on all interfaces (0.0.0.0/0)
![image](https://github.com/user-attachments/assets/76304685-062f-41df-ac18-092174428aa2)

sudo systemctl restart ssh



On rw01, create a dedicated keypair that will only be used for ssh access to jump. make sure to name the keypair something other than the default and add a comment indicating its purpose.  Make sure to add a passphrase when prompted.

```
ssh-keygen -t rsa -b 4096 -C "ssh to jump"
name of file: jump-charlotte
```

create a passwordless user called `charlotte-jump` on jump.  Copy over the public component of the jump keypair you just created on rw01 to the new user's `.ssh/authorized_keys` file. 



# network firewalls 1

## Configuring fw01
- Create and link firewall zones to interfaces (eth0, eth1, eth2)
```
set zone-policy zone WAN interface eth0
set zone-policy zone DMZ interface eth1
set zone-policy zone LAN interface eth2
```

### WAN and DMZ firewalls
In the illustration below, we have created firewalls for WAN to DMZ and DMZ to WAN, 
we are going to lock them down with a default drop directive, and we will log violations of the firewall rules. 
We have also assigned firewalls to the respective direction of communication between zones.

Firewalls for WAN and DMZ
```
set firewall name WAN-to-DMZ default-action drop
set firewall name DMZ-to-WAN default-action drop
set firewall name WAN-to-DMZ enable-default-log 
set firewall name DMZ-to-WAN enable-default-log
```

Assigning Firewalls to Zones
```
set zone-policy zone WAN from DMZ firewall name DMZ-to-WAN 
set zone-policy zone DMZ from WAN firewall name WAN-to-DMZ 
```


On fw01, monitor your firewall logs with the following command:
`tail -f /var/log/messages | grep WAN`





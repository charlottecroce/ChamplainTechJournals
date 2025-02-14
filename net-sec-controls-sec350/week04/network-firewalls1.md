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


## Allow http inbound
```
set firewall name WAN-to-DMZ rule 10 description "Allow HTTP from WAN to DMZ"
set firewall name WAN-to-DMZ rule 10 action accept
set firewall name WAN-to-DMZ rule 10 destination address 172.16.50.3
set firewall name WAN-to-DMZ rule 10 destination port 80
set firewall name WAN-to-DMZ rule 10 protocol tcp
```
## allow return traffic
this won't work if you try to ping/curl, because traffic back out to WAN is still blocked
these commands will allow established connection through DMZ-to-WAN
```
set firewall name DMZ-to-WAN rule 1 action accept
set firewall name DMZ-to-WAN rule 1 state established enable
```


>[!Note]
>We will reserve rule 1 for two conditions.  The first is to allow established connections back out again, the second would be to have an open rule where all connections are allowed.  Typically this would be the only rule in such a firewall.

## DMZ and LAN Traffic Firewalls

```
set firewall name LAN-to-DMZ default-action drop
set firewall name DMZ-to-LAN default-action drop
set firewall name LAN-to-DMZ enable-default-log 
set firewall name DMZ-to-LAN enable-default-log
```

Assigning Firewalls to Zones
```
set zone-policy zone LAN from DMZ firewall name DMZ-to-LAN 
set zone-policy zone DMZ from LAN firewall name LAN-to-DMZ 
```

### allow ports 1514 and 1515
```
set firewall name DMZ-to-LAN rule 10 description "wazuh agent communication with server"
set firewall name DMZ-to-LAN rule 10 action accept
set firewall name DMZ-to-LAN rule 10 destination address 172.16.200.10
set firewall name DMZ-to-LAN rule 10 destination port 1514,1515
set firewall name DMZ-to-LAN rule 10 protocol tcp
```

### allow return traffic from DMZ
```
set firewall name DMZ-to-LAN rule 1 action accept
set firewall name DMZ-to-LAN rule 1 state established enable
```


### allow return traffic from LAN
```
set firewall name LAN-to-DMZ rule 1 action accept
set firewall name LAN-to-DMZ rule 1 state established enable
```

## lan to wan?
yes, clients usually need direct access to internet. we will have to configure proxies for this later\
Create a default LAN to WAN firewall and associate it with the appropriate zone policy.  This firewall will have only one rule allowing LAN clients to initiate WAN connections.
```
set zone-policy zone WAN from LAN firewall name LAN-to-WAN
set firewall name LAN-to-WAN default-action drop
set firewall name LAN-to-WAN enable-default-log
set firewall name LAN-to-WAN rule 1 action accept
```
### allow return traffic WAN to LAN
```
set zone-policy zone LAN from WAN firewall name WAN-to-LAN
set firewall name WAN-to-LAN default-action drop
set firewall name WAN-to-LAN enable-default-log
set firewall name WAN-to-LAN rule 1 action accept
set firewall name WAN-to-LAN rule 1 state established enable
```

## LAN to DMZ
As communication between LAN and DMZ is currently broken, we need to create a firewall, assign to the appropriate zone policy and adjust it to only allow the traffic we want to go through.  We want wks01 to be able to browse to web01 and we want mgmt01 to ssh into anything on the DMZ.

With that in mind, create firewall rules on LAN-TO-DMZ that allows 
- 80/tcp from LAN to web01.

```
set firewall name LAN-to-DMZ rule 10 description "Allow HTTP from LAN to DMZ"
set firewall name LAN-to-DMZ rule 10 action accept
set firewall name LAN-to-DMZ rule 10 destination address 172.16.50.3
set firewall name LAN-to-DMZ rule 10 destination port 80
set firewall name LAN-to-DMZ rule 10 protocol tcp
```
- 22/tcp from mgmt01 to the DMZ
```
set firewall name LAN-to-DMZ rule 20 description "Allow SSH from MGMT-01 to DMZ"
set firewall name LAN-to-DMZ rule 20 action accept
set firewall name LAN-to-DMZ rule 20 source address 172.16.150.10
set firewall name LAN-to-DMZ rule 20 destination port 22
set firewall name LAN-to-DMZ rule 20 protocol tcp
```


# host discovery

## ping (simple/not efficient)
```
ping <ip>
```
[pingsweep.sh](week02/pingsweep.sh)


## fping (better for scanning with ICMP)
```
fping -g 10.0.5.2 10.0.5.50
```
[pingsweep2.sh](week02/pingsweep2.sh)


## nmap (most efficient)
- `-sn`: host discovery mode
- `-oG`: output to greppable format
**- remember to run nmap as sudo**
```
sudo nmap -sn 10.0.5.2-50 -oG sweep3.txt
```
[pingsweep3.sh](week02/pingsweep3.sh)

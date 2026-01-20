# host discovery

## ping (simple/not efficient)
```
ping <ip>
```
[pingsweep.sh](pingsweep.sh)


## fping (better for scanning with ICMP)
```
fping -g 10.0.5.2 10.0.5.50
```
[pingsweep2.sh](pingsweep2.sh)


## nmap (most efficient)
- `-sn`: host discovery mode
- `-oG`: output to greppable format
**- remember to run nmap as sudo**
```
sudo nmap -sn 10.0.5.2-50 -oG sweep3.txt
```
[pingsweep3.sh](pingsweep3.sh)



# lab reflections
it tooks a while for me to figure out formatting for nmap scans, i was trying to use sed but it was more complicated than it needed to be. the `-oG` output flag makes grepping the output much easier

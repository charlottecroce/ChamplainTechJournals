# nmap
```
nmap <target> <flags>
```

## Ports
- `-p 443`
- `-p 22,3389`
- `-p 1-6000`

## Scan type
- `-sT`: TCP connect
- `-sS`: TCP stealth scan (don't complete connection)
- `-sU`: UDP Scan

## Service Detection
- `-sV`: service version
- `-O`: OS detection
- `-A`: aggressive (OS, version, scripts, traceroute)

## other
- `-Pn`: skip host discovery
- `-sL`: list targets

## output
- `-oG`: output greppable format

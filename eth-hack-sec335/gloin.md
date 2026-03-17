# gloin

## Target IP Address
10.0.5.31 (from dns-resolver.sh)
## Open Ports
```
└─$ sudo nmap 10.0.5.31 -sS -sV -p- -T4   
Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-17 16:38 EDT
Nmap scan report for 10.0.5.31
Host is up (0.0012s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
443/tcp  open  ssl/http      Apache httpd 2.4.51 ((Win64) OpenSSL/1.1.1l PHP/7.3.31)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```
22(ssh), 443(https), and 3389(rdp). target is using windows OS

## Discovered Vulnerability
## How you achieved a foothold
## How you achieved root/Administrative level compromise
## User Flag
## Root Flag
## How might the vulnerabilities be mitigated by the systems administrator and developer?

## Reflection

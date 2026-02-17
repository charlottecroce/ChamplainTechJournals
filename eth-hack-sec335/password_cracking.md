
## john the ripper (JTR)

unshadow - combine /etc/passwd and /etc/shadow
```
unshadow etc_passwd.txt etc_shadow.txt > passwd_with_hashes.txt
```
simplest way to crack completed passwd file
```
john passwd_with_hashes.txt
```

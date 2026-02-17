
## john the ripper (JTR)

unshadow - combine /etc/passwd and /etc/shadow
```
unshadow etc_passwd.txt etc_shadow.txt > passwd_with_hashes.txt
```
simplest way to crack completed passwd file
```
john --users=gandalf,boromir,galadriel --worlist=/usr/share/wordlists/rockyou.txt passwd_with_hashes.txt
```

## hashcat
- `-m` = hash type
  - 0: md5
  - 1000: NTLM
  - 1800: sha512
-a (Attack Mode): Defines the method of attack.
  - 0 = Straight (Dictionary)
  - 1 = Combination
  - 3 = Brute-force / Mask
  - 6 = Hybrid Wordlist + Mask
  - 7 = Hybrid Mask + Wordlist
```
sudo hashcat -m 1800 -a 0 -o cracked.txt unshadowed.txt small.txt
```

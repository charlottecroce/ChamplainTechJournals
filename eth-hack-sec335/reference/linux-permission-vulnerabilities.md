# Linux Permission Vulnerabilities

### search for SUID programs in linux system
SUID programs run with the owner's permissions. this can be exploited for privilege escalation. normal programs start their permissions code with 0 (eg 0755), but SUID programs start their permissions code with 4 (eg 4755)
```
find / -perm -4000 -type f 2>/dev/null
```

### search for files with world write permissions
```
find /etc -type f -perm /o=w 2>/dev/null
```
if searching entire system, exclude `/sys` and `/proc`
```
find / -type f -perm /o=w 2>/dev/null | grep -v "^/sys" | grep -v "^/proc"
```

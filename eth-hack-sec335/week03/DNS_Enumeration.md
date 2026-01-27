## zone transfer
```
dig axfr @<dns-server> <domain>
dig axfr @nsztm1.digi.ninja. zonetransfer.me
```
to parse A records out of zone transfer result
```
... | awk '$4=="A" {print $1, $5}'
```

## nslookup
```
nslookup <target> <dns server to use for query>
```

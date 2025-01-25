# lab01- Network Management

## nmon1-charlotte
- setup with hostname, username, networking (10.0.5.11, remember: add `charlotte.local` to search domain)
- add record to DNS manager
![image](https://github.com/user-attachments/assets/40d632c5-18c8-42b0-a938-19f6aabce1d0)

```
I had trouble reaching the internet on nmon1, then realized fw01 couldn't reach the internet as well.
idk what happened but I rebooted fw01 and it worked again
```

## enable SNMP services on pfSense
- web dashboard (10.0.5.2)
- services -> SNMP

![image](https://github.com/user-attachments/assets/27e9470d-e84b-4e8b-8076-cfcbc9b54dea)
![image](https://github.com/user-attachments/assets/bcdeb3dd-1245-4fc0-aff3-0a84cb383c8f)

- restart SNMP service
![image](https://github.com/user-attachments/assets/727824d9-510f-4235-8e62-7360a41ebae2)


## Install and Test SNMP Client on nmon01
`sudo yum install net-snmp-utils`
![image](https://github.com/user-attachments/assets/c2924ebd-c975-4cbf-9b0e-b26e36954fdb)

## Install SNMPD (a SNMP Server) on web01

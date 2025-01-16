# Lab00 - Routing and Windows   

Our goal is to build a realistic server environment consisting of a routed network (LAN and WAN) as well as introduce Server 2019 Desktop and Core and the systems required to manage them.

## FW01 and WKS01
- [use this doc](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab01-environment-setup.md)

## AD01 
- (admin password is `password123!`)
- `sconfig` \
![image](https://github.com/user-attachments/assets/b42fc4c4-07fe-44e1-ae48-59a1ea275408)

- Invoke powershell and install Active Directory: `Install-WindowsFeature AD-Domain-Services -IncludeManagementTools` \
![image](https://github.com/user-attachments/assets/2a087f38-8b59-4497-9162-1631205d0150)

- Install the Forest: `Install-ADDSForest -DomainName charlotte.local` \
![image](https://github.com/user-attachments/assets/b295e94c-3da4-4dbe-98d5-45f25a4da00a)

- You should be in a domain now \
![image](https://github.com/user-attachments/assets/73076712-88fa-4c39-866b-da138c52002d)

### creating domain users (one user, one admin):
- `net user charlotte.croce password123! /ADD /DOMAIN`
- `net user charlotte.croce-adm password123! /ADD /DOMAIN`
- `net group "Domain Admins" charlotte.croce-adm /ADD /DOMAIN`


## MGMT01
MGMT01 is a Server 2019 with GUI.  Its job will be to remotely manage any server core systems. 
password: `password123!` \
![image](https://github.com/user-attachments/assets/b752ce4c-f831-4619-b563-9a2ff9eb57c5)

to join domain:
- `sconfig` -> 1 -> D -> charlotte.local -> Administrator -> type Administrator password in prompt -> restart
- login as the charlotte.croce-adm domain user

adding ad01 to management scope
- server manager - add roles and features
- add the following features: \
![image](https://github.com/user-attachments/assets/25634b91-4a27-4ff5-a218-337fab157561)
![image](https://github.com/user-attachments/assets/f1b9d632-2664-4209-beae-3ee167b93a76)

- create DNS records: [use this doc](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab02-dns%2Badds-role.md)
- note: it's easier to create the reverse lookup zone first, as PTR records will be created automatically when you create a new A record, although you will still have to manually create some PTRs
![image](https://github.com/user-attachments/assets/1fc7982f-2d40-49d2-8264-356db5fb0d8c)
![image](https://github.com/user-attachments/assets/d750c565-6a8c-4867-8da3-949046bb5a1e)

- finally, join wks01 to the domain
- before doing so, we must change the DNS server to 10.0.5.5, to recognize charlotte.local
![image](https://github.com/user-attachments/assets/f7c0d739-296c-4fab-96b2-4afe4439aee6)


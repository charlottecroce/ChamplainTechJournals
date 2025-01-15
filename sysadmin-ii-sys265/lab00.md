Lab00 - Routing and Windows   

Our goal is to build a realistic server environment consisting of a routed network (LAN and WAN) as well as introduce Server 2019 Desktop and Core and the systems required to manage them.

- setup FW01 and WKS01 [use this doc](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/sysadmin-i-sys255/lab01-environment-setup.md)

## setup AD01 
- (admin password is `password123!`)
- `sconfig` \
![image](https://github.com/user-attachments/assets/b42fc4c4-07fe-44e1-ae48-59a1ea275408)

- Invoke powershell and install Active Directory: `Install-WindowsFeature AD-Domain-Services -IncludeManagementTools` \
![image](https://github.com/user-attachments/assets/2a087f38-8b59-4497-9162-1631205d0150)

- Install the Forest: `Install-ADDSForest -DomainName charlotte.local` \
![image](https://github.com/user-attachments/assets/b295e94c-3da4-4dbe-98d5-45f25a4da00a)


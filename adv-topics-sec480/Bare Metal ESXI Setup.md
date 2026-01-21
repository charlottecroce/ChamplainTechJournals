# Bare Metal ESXI Setup

## installing ESXI on supermicro server
- download ISO from `CYBER-SHARE(X:)`
- install to USB via rufus
<img width="465" height="590" alt="{752F5C39-E359-436B-A26B-84EFC876E145}" src="https://github.com/user-attachments/assets/ce224558-fe6d-4216-8f79-bfabb116c659" />

- put USB in physical server
- go to IPMI interface (192.168.3.155)
- remote control > iKVM
- powercontrol > set power reset
- open virtual keyboard - spam F11
- select UEFI: <USB>
<img width="296" height="281" alt="{9F2BF516-1566-40AD-8C8A-881CEDCBB079}" src="https://github.com/user-attachments/assets/b29106c5-ac59-49d6-9314-72117b70a8e5" />

- install on smaller drive
<img width="669" height="297" alt="{352C96E1-2EF9-4546-ACF4-4B2B5F2D89CD}" src="https://github.com/user-attachments/assets/8724be06-2573-4ffd-8885-cb554df402b1" />

- REMEMBER ROOT PASSWORD
- after installation, remove USB from server and reboot from IKVM


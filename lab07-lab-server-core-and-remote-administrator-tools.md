# Lab07 - Lab Server Core & Remote Administrator Tools

### joining fs01-nathan to domain

* `sconfig` - server configuration
* edit default configs to match the screenshots below

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/427cb3c7-be4e-4476-b5ec-3be0fa8e5557) ![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/e883de4b-b135-4397-b879-547eff903860)

* join domain nathan.local using nathan.croce-adm user

### Allowing ad02 remote access to fs01

* on ad02 - server manager - manage - add roles and features
* skip to features section
* check remote server administration tools / role administration tools / file services tools / file server resource manager tools
* install
* add fs01 to all servers

### Use RSAT to add to FS01 and create a Sales Users share

* on ad02 - all servers - rc fs01 - add roles and features
* skip to server roles
* file and storage services / file and iSCSI services / check file server & file server resource manager
* install
* Run the following Net Shell command on fs01 to open the firewall for managing the File Server `netsh advfirewall firewall set rule group=”Remote File Server Resource Manager Management” new enable=yes`
* on ad02 - server manager - file and storage services - servers - rc fs01 - file server resource manager
* on ad02 - server manager - file and storage services - shares - new share
* SMB quick share - located on fs01

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/0f0e8792-547e-4d09-b136-416cc68f8a48)

* skip to create
* edit permissions and give sales-users full control over share

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/e44fc017-9960-4282-9772-5926c9c34c0d)

### mapping network share to drive letter

* on ad02 - group policy management - ... - SYS255 - groups - Create GPO and link it here (I name it 'Mapped Drive')
* check enforced on the GPO (not shown in ss below)

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/c41c4ff7-9c7e-48e3-8531-3cc93e995dd7)

* edit GPO
* User Configuration -> Preferences -> Windows Settings -> Drive Mappings - rc Drive Maps - new - mapped drive

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/bd841f6f-d3c4-4824-80f0-889e9d89f2c3) ![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/dd8df225-f217-4d95-9e09-7ad27645ab38)

* common tab - targeting
* new item - organization unit

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/5d9680e0-f5f0-45ff-8d3e-2ca78a0f796c)

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/a45b642b-a8bc-449c-9a19-91d140e3e041)

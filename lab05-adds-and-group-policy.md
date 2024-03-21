---
description: This week we created organizational units and group policy on our AD server
---

# Lab05 - ADDS & Group Policy

### Create organizational units and add users/computers/groups

* Server Manager -> Active Directory Users and Computers
* rc nathan.local -> new -> Organizational Unit (named SYS255)
* rc SYS255, create three child OUs (Accounts, Computers, and Groups)
* add users Alice, Bob, and Charlie to SYS255/Accounts (default password is Pass123!)
* move WKS01-NATHAN from nathan.local/Computers to nathan.local/SYS255/Computers
* within the SYS255\Groups OU, add a global security group called custom-desktop with users Alice and Bob (not Charlie) as members

### Create group policy

* Server Manager -> Group Policy Management
* rc nathan.local/SYS255 -> Create GPO in this domain... (name it sys255-desktop)
* click sys255-desktop, under Security Filtering, add the custom-desktop global security group
* remove Authenticated Users
* add Domain Computers

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/7702b2de-1b0e-4bef-a49b-8cd89acd144b)

* Delegation tab -> Advanced -> Domain Computers -> Uncheck Apply Group Policy and Select Deny

### Edit group policy

* rc sys255-desktop - > Edit

#### remove the recycling bin

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/00b26c07-2662-47d1-a39f-aea911f668a3)

#### disable last login

* create a GPO under SYS255/Computers
* aplly security filtering to only domain computers
* rc DisableLastLogin -> Edit

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/6bdac006-5ab7-4cf8-b523-11860a85e377)

### Useful commands

`gpresult /r` - shows a summary of group policy on a workstation\
`gpresult /scope computer /r` - shows a summary of computer-specific group policy\
`gpupdate /force` - forces a group policy update

### Network Diagram

https://app.diagrams.net/#Hnathancroce%2FTechJournalsSYS-255%2Fmain%2FNetworkDiagram.drawio

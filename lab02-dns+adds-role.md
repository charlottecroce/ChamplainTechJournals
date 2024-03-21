---
description: >-
  In this lab, we created an Active Directory Domain Server on our Windows 2019
  Server (10.0.5.5)
---

# Lab02 - DNS+ADDS Role

## Domain vs. Local Administrator

Local administrators have power within the singular Windows OS, while Domain administrators have power over items within the AD domain

## Installing the ADDS Role on Windows Server

* go to Server manager
* Manage -> Add Roles and Features
* check `Active Directory Domain Services` and install dependencies as well
* continue through wizard and install

## Configure our server to be the primary domain controller for our domain

* click `Promote this server to a domain controller`
* `Add a new forest` - nathan.local
* set DSRM password
* continue through wizard and install

## Create Forward Lookup DNS Records

* go to DNS Manager
* DNS -> ad01-nathan.nathan.local -> Forward Lookup Zones -> right click nathan.local -> New Host
* PTR records will not work right now /bc there is no reverse lookup zone

## Create Reverse Lookup DNS Records

* go to DNS Manager
* DNS -> ad01-nathan.nathan.local -> right click Reverse Lookup Zones -> New Zone
* enter Network ID (10.0.5.) when prompted
* update PTR records on A records, refresh, and PTR records should appear in Reverse Lookup Zones

## Create a user in AD

* server manager -> AD DS -> right click server -> Active Directory Users and Computers
* nathan.local -> right-click Users -> New -> User

## Add a user to the domain admin group

* right click created user -> add to a group
* type 'Domain Admins'

## Add a computer to the domain

* control panel -> system and security -> system -> change settings
* change from workgroup to domain

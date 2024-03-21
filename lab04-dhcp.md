---
description: >-
  this week we configured dhcp01-nathan to run the dhcp server. now wks01 uses
  dhcp rather than static IP assignment
---

# Lab04 - DHCP

## DHCP configuration

* connect to dhcp01-nathan via puTTY
* `sudo yum install dhcp`
* configure `/etc/dhcp/dhcpd.conf` file

![image](https://github.com/nathancroce/TechJournalsSYS-255/assets/90940521/4d235432-357a-48d8-9241-dca6a70874b5)

* start\&enable dhcp
* configure dhcp on firewall
* configure wks01-nathan to use DHCP instead of static IP

#### to start dhcp

`systemctl start dhcpd`

#### to check status of dhcp

`systemctl status dhcpd`

#### configure dhcp to start on boot

`systemctl enable dhcpd`

#### configure dhcp on firewall

* `firewall-cmd --add-service=dhcp --permanent`
* `firewall-cmd --reload`
* `firewall-cmd --list-all`

#### search for dhcp logs from wks01-nathan

`sudo cat /var/log/messages | grep wks01-nathan`

#### release dhcp

`ipconfig /release`

#### renew dhcp

`ipconfig /renew`

#### filtering dhcp messages in wireshark

`udp.port==67`

## Disable root access via ssh

* `nano /etc/ssh/sshd_config`
* change `PermitRootLogin` from yes to no and uncomment
* `systemctl restart sshd`

## File Permissions

#### how to create a group

`groupadd [groupname]`

#### how to add a user to a group

`usermod -aG [groupname] [username]`

#### how to change the owner of a file

`chown filename [username]`

#### how to change the group of file

`chgrp filename [groupname]`

## Changing file permissions

#### Method 1: using bit values

* Read: 4
* Write: 2
* Execute: 1 Add up the numbers to set permissions for each accessor (owner/group/everyone else)

example: `chmod 640 file.txt` give read/write to owners, read to group members, and no access to everyone else

#### Method 2: adding/removing file permissions individually

* `chmod u+/-(r/w/x) [filename]` - users (owner)
* `chmod g+/-(r/w/x) [filename]` - group
* `chmod o+/-(r/w/x) [filename]` - others (everyone else)

example: `chmod g+w file.txt` gives write permissions to the group of `file.txt`

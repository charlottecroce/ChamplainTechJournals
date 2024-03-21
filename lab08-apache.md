---
description: In this lab, we set up an Apache web server on WEB01
---

# Lab08 - Apache

## Apache Server Installation & Configuration

### Configure WEB01

* `nmtui`
* IP address is 10.0.5.10
* setting alternate DNS to 8.8.8.8 made initial connectivity work (idk why)
* remember to add A and PTR records to DNS server

### Install httpd

* `yum install httpd`
* `firewall-cmd --add-service=http --permanent`
* `firewall-cmd --add-service=https --permanent`
* `firewall-cmd --reload`
* `systemctl start httpd`
* `systemctl enable httpd`
* comment out all lines in `/etc/httpd/conf.d/welcome.conf`
* add _index.html_ file to `/var/www/html/`
* the contents of _index.html_ should be what searching `http://web01-nathan` in a browser will give you

### Install PHP

* `yum install -y php`
* `systemctl restart httpd`
* add _index.php_ file to `/var/www/html/`

## Linux Domain Join

* `sudo yum install -y realmd samba samba-common oddjob oddjob-mkhomedir sssd`
* `sudo realm join --user=nathan.croce-adm@nathan.local nathan.local`
* `realm list`

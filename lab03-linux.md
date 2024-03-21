---
description: >-
  In this lab we set up the DHCP server in Linux, but we haven't added any DHCP
  functionality yet, just networking configurations and adding a user
---

# Lab03 - Linux

## Network Configuration

* login as root
* `nmtui`
  * Edit a connection -> enter configs (remember to set search domain to nathan.local)
  * Set system hostname: dhcp01-nathan
* `systemctl restart network`
* `exit`
* login as root again
* if not done already, create a privileged user so you're not always using root

## mntui

* network manager TUI
* used to set up network configuration

## creating privileged user in Linux

* `useradd nathan`
* `passwd nathan`
* `usermod -aG wheel nathan`

## ipconfig DNS commands

* `/flushdns`: clears DNS cache and forces the computer to regain all DNS entries from the DNS server
* `/registerdns`: re-registers all domain names and IP addresses

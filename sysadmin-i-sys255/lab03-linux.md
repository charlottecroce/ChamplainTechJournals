---
description: >-
  In this lab we set up the DHCP server in Linux, but we haven't added any DHCP
  functionality yet, just networking configurations and adding a user
---

# Lab03 - Linux Setup

## mntui
* network manager TUI
* used to set up network configuration & can change hostname
* (remember to set search domain to charlotte.local)
* `systemctl restart network` or `systemctl restart NetworkManager` to restart network after config change


## set hostname
`hostnamectl set-hostname dhcp01-charlotte`

## creating privileged user
* `useradd charlotte`
* `passwd charlotte`
* `usermod -aG (wheel/sudo) charlotte` - RH=wheel, Debain=sudo


## ipconfig DNS commands
* `/flushdns`: clears DNS cache and forces the computer to regain all DNS entries from the DNS server
* `/registerdns`: re-registers all domain names and IP addresses

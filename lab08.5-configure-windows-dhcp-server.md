---
description: >-
  In this lab, we configured a Windows DHCP Server on FS01, which is accessible
  via AD02 RSAT
---

# Lab08.5 - Configure Windows DHCP Server

## Install DHCP on FS01

* AD02 - all servers - rc FS01 - Add Roles and Features
* roles - check DHCP server
* continue to install
* complete DHCP configuration

## Add RSAT to AD02

* Add Roles and Features
* select AD02
* Features - Remote Server Administration Tools - Remote Server Administration Tools - DHCP Server Tools
* continue to install

## Configure DHCP on FS01

* rc FS01 - DHCP Manager
* add server - select FS01
* rc IPv4 - New Scope
* configs are pretty self-explanatory (remember to add 10.0.5.6 to DNS)

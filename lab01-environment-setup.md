---
description: >-
  In this lab, we set up our Windows workstation and PfSense firewall on
  vSphere.
---

# Lab01 - Environment Setup

## Add a Network Adapter in VSphere:

* Power off the machine
* VM Hardware Section -> Edit
* Add New Device -> Network Adapter

## Rename a Windows Computer

* In File Explorer, right-click on “This PC”
* “Properties” -> “Change Settings”
* Click “Change” next to “To rename this computer…”

## Add a user on Windows

* Computer Management -> Local Users and Groups -> Users
* Right Click -> New User

## Add a User to a Group on Windows

* Go to user Properties -> Member Of -> Add
* Type the group name i.e. WKS01-NATHAN\Adminstrators
* Check names, if the text entered is a valid group, the text should underline

## Change IP Address on Windows

* Go to Network and Internet settings -> Change adapter options
* Right-click on network adapter - “properties”
* Double-click IPv4 setting

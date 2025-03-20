# Lab 7.1 Assessment Prep 
Several systems in your current environment will be removed the day before the assessment (3/27), first thing in the morning.
- **rw01** -> **traveler**
- **fw01** -> **edge01**
- **web01** -> **nginx01**

```
You are on your own for the assessment.
Open notes and internet, just no open neighbor.
This is really a test of your notes.
You will be getting new VM's.
Don't be late, as you will likely need the full time.
```

## fw01 configuration Backup
- **edge01**: (this new firewall will be very close in configuration).
- You might also consult your the example week 4 configurations [here](../configs/fw01/fw01.config.week04.txt)

- Provide the raw commands necessary to reconstitute your firewall: (Remember, there may be some adjustments in IP addresses and rules for your internal systems.)


## Assessment Description
For the assessment, you will be given a 3 zone network to configure that consists of:
- **traveler**.  A WAN based road warrior user running Windows 10. (this replaces the linux rw01)
- **edge01**.  A vyOS Firewall with three interfaces (WAN, DMZ, LAN).  You will need to add an interface using vCenter. (this replaces fw01)
- **nginx01**.  A DMZ based nginx web server running Ubuntu (this replaces web01 and apache)
- **dhcp01**.  A LAN based dhcp server running Ubuntu

## Requirements
- All systems should have an accurate hostname.
- All Linux systems should have a named sudo or administrator user.
- The two new ubuntu systems do not have a host firewall enabled, this is ok (for now)
- wks1, mgmt01 should be able to surf the internet.
- wks1, mgmt01 should be able to navigate to nginx01
- mgmt01 should be able to ssh to nginx01
- nginx01 and dhcp01 should have wazuh agents installed and be able to connect to wazuh
- nginx01 should have a custom web page (practice this on jump)
- traveler should be able to get to nginx01's custom test page by navigating to edge01's WAN IP address.
- traveler should be able to perform ssh keybased authentication with jump.  Traveler is a Windows box, but ssh on powershell is nearly exactly the same as linux to include key generation.  You will need to add a new public key to authorized_keys.
- dhcp01 should serve a pool of dhcp addresses to the LAN from .100 to .150.
- WKS1 should use dhcp addressing

## Hints
- You do not need to work serially through this assessment, it is the end result that matters. If you are waiting for a reboot on traveler, then start configuring your other servers.
- Get all communications working BEFORE creating zones and locking down the firewalls.  It's terribly difficult to debug both services and network firewalls at the same time.
- Make sure to link your firewalls to the appropriate From and To zones.
- Make sure you have the correct netmask on all Linux systems.
- Restart any service if you touch a configuration file (network, nginx, rsyslog, etc…).
- Make sure you include the appropriate vsphere label on all deliverables where your name is not obvious in the console.
- Check every VM's network settings to make sure they are on the correct segment.
- Don't forget to look at `/var/log/messages` to debug firewall issues.
- Do not try to use the default gateway address 10.0.17.2 as your WAN interface IP address as this will cause problems for other students and might be embarrassing.


## Nginx Web Server
Practice this on jump (it is an ubuntu box).


## Ubuntu DHCP Server
You can also practice this on jump, just move it to LAN, change the IP to something else and see if you can get wks01 to use dhcp services for IP, Netmask, Gateway and DNS settings.  Make sure to reset wks01 to static.

## Traveler is a Windows System
You should research how to create a keypair using powershell or putty and make sure you can adjust jumps authorized_keys file to use your new windows public key.

## Deliverable 3.  Practice this on either mgmt02 or wks01.  Figure out how to create a keypair using either powershell or PuTTY, transfer the public portion to one of your linux systems and demonstrate a passwordless login from windows to a linux system.

## Clearing the firewall configuration
You should rehearse vyos commands by clearing your current configuration.  The following commands will do that.  Note, this configuration will likely have the vyos/vyos password combination because that is what it ships with.

```
configure
load /opt/vyatta/etc/config.boot.default
commit
save

# to save and load a backup config file
save backup_1
load /config/backup_1
```

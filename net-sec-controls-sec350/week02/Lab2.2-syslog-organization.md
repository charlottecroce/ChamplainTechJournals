# Lab 2.2 - Syslog Organization on log01

## setup mgmt01
- on LAN
- ip: 172.16.150.10
- DG & DNS: 172.16.150.2

### configure fw01 with the LAN
#### NAT rules on fw01, to set NAT for LAN to WAN
```
set nat source rule 20 description "NAT FROM LAN to WAN"
set nat source rule 20 outbound-interface eth0
set nat source rule 20 source address 172.16.150.0/24
set nat source rule 20 translation address masquerade
```
#### DNS forwarding from LAN to WAN
```
set service dns forwarding listen-address 172.16.150.2
set service dns forwarding allow-from 172.16.150.0/24
```
mgmt01 should now be able to ping google.com

### Install chrome remote desktop on mgmt01
- open chrome
- sign in with school email and turn on sync
- go to remotedesktop.google.com, install the app if you want
- on main host (laptop, go to `https://g.co/crd/headless`), download and install the package: 
  - there might be dependency issues, this command worked on my computer: `sudo apt install libutempter0 xbase-clients xserver-xorg-video-dummy xvfb`
  - `sudo dpkg -i google-chrome-stable_current_amd64`
- still on main host, click next and copy the command for the remote OS (in our case, debian)
- paste it in the remote terminal, and create a PIN
- at this point you should be able to access mgmt01 via chrome remote desktop, you might need to update CRD on mgmt01 first though, but we know how to do that ^
- IMPORTANT: log out of the remote computer before attempting to connect

## log organization on log01
Having all of our remote logs stuffed into log01's  /var/log/messages or /var/log/secure is not helpful. Remote logs should be segregated and ideally stored on reliable and redundant storage in a manner that supports dealing with discrete event types. We are going to store logs in a directory hierarchy in order to provide this organization.

- re-comment the input modules from lab 1.1
![image](https://github.com/user-attachments/assets/a51c6beb-41a7-4885-a285-61885f073995)
- create a new config file call sec350.conf:
![image](https://github.com/user-attachments/assets/c12ab0af-4ef2-4904-9ede-9d4d96a65122)
- copy that file to /etc/rsyslod.d/: `sudo cp sec350.conf /etc/rsyslog.d/`

```
This configuration file (03-sec350.conf) will dynamically create and name files based upon hostname,
date and process name. Input over udp 514 is associated with the RemoteDevice ruleset which in turn
uses the dynamic template configuration called “DynFile”.
``` 
testing \
![image](https://github.com/user-attachments/assets/37f2c335-0611-42c9-962a-62a4681eeae5)
![image](https://github.com/user-attachments/assets/3b863e99-1ae4-4d29-91cb-1a3b187aab5f)

## web01: Logging Authorization Events
Modify the rsyslog client configuration on web01 so that authentication events are forwarded to our log server. the line `authpriv.* @172.16.50.5` will send all authpriv logs to the remote server(log01)
![image](https://github.com/user-attachments/assets/59be1bd2-d915-4360-9595-f0d32d68e030) \
after sshing from rw01>web01(with failed attempts), we can see this in the sshd.log file \
![image](https://github.com/user-attachments/assets/f45b745c-6aff-4cd6-86dd-0ddb13256267)

## fw01: Logging Authorization Events
We are going to adjust the vyos configuration to send authentication messages from fw01 to log01.  Note, vyos does produce a ton of useless authentication messages which we are going to have to deal with at some point.
- first, [change the default password](https://github.com/charlottecroce/ChamplainTechJournals/blob/main/net-sec-controls-sec350/week01/vyos.md#change-password) : `set system login user vyos authentication plaintext-password password123!`
- `set system syslog host 172.16.50.5 facility authpriv level info` \
![image](https://github.com/user-attachments/assets/57d3e4d5-2d74-45c7-91e1-7e0066bcaf10) \
![image](https://github.com/user-attachments/assets/26d035b6-8587-4277-ac33-3b4824459cc8)



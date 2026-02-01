# Milestone 2.2 - vCenter

The rough steps you will take:
- Download the vCenter to your datastore
- Run the installer on xubuntu-wan
- Create a datacenter called 480-charlotte
- Add your superX esxi system to your datacenter as a host

## preperation
On MGMT1, you will need to change your IPv4 settings use your 
domain controller as DNS server with a search domain of yourname.local
```
# find connections (prob "Wired connection 1")
nmcli connection show --active

sudo nmcli connection modify "Wired connection 1" ipv4.dns "10.0.17.4"
sudo nmcli connection modify "Wired connection 1" ipv4.dns-search "charlotte.local"

# reset network (do this from esxi -- this will kick you out of CRD)
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection up "Wired connection 1"
```

- add this line to `/etc/hosts`
```
192.168.3.205   super5.cyber.local
```

- Ensure your ESXI host is synched to ntp.org
  - Host->manage>time & date> NTP Server: pool.ntp.org
  - Go to services, find NTP service, ensure it is started and set to start/stop with host

## installing vcenter
- On MGMT1 - Mount your VCSA ISO (don't worry, this isn't a normal ISO, it will create a new VM)
- Once mounted you can navigate to /media/user/VMWare VCSA/vcsa-ui-installer/lin64
- Then you can run ./installer (from cli)
- Run through installer (this may take some time, 2 stages…)
- **Thin Disk!!**, select the new datastore you created (if you have it)
- `480-internal` network
Be careful, don’t lose your VCSA root pass OR default SSO admin pass!!
You can re-use the same pass for both
Ryan can’t reset it for you
Create your default vcenter domain & admin
administrator@vsphere.local is a good default


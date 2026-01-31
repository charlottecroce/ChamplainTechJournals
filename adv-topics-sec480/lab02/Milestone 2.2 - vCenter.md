# Milestone 2.2 - vCenter

The rough steps you will take:
- Download the vCenter to your datastore
- Run the installer on xubuntu-wan
- Create a datacenter called 480-charlotte
- Add your superX esxi system to your datacenter as a host


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



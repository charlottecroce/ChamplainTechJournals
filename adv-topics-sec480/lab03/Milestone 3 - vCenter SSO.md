# Milestone 3 - vCenter SSO
vcenter management console: (https://vcenter.charlotte.local:5480 | user=administrator@vsphere.local)

## update vcenter(failed)
vcenter management ui >  update, stage & update
- Broadcom has changed update urls: https://adrian.heissler.at/2025/04/broadcom-changes-download-urls-for-vmware-products/

## SSO
Log in to the vSphere Client(not management consolve) as administrator@vsphere.local
- navigate to Menu > Administration > Single Sign-On > Configuration, select Active Directory Domain, click JOIN AD, enter domain credentials (administrator:pw)
- reboot from management console
- add windows AD identity source

<img width="849" height="361" alt="{E8CF2BA0-CB11-4207-80A4-9D89F203F231}" src="https://github.com/user-attachments/assets/04450414-bb03-493b-bf20-62c16eb26f9f" />
- navigate to Menu > Administration > Single Sign-On >  Users and Groups, groups, add Domain Admins from charlotte.local to administrators
- you can now login to vcenter with charlotte-adm@charlotte.local

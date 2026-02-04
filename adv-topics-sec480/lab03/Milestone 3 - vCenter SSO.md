# Milestone 3 - vCenter SSO
vcenter management console: (https://vcenter.charlotte.local:5480 | user=administrator@vsphere.local)

## update vcenter(failed)
vcenter management ui >  update, stage & update
- Broadcom has changed update urls: https://adrian.heissler.at/2025/04/broadcom-changes-download-urls-for-vmware-products/

## SSO
Log in to the vSphere Client(not management consolve) as administrator@vsphere.local
- navigate to Menu > Administration > Single Sign-On > Configuration, select Active Directory Domain, click JOIN AD, enter domain credentials (administrator:pw)
- reboot from management console


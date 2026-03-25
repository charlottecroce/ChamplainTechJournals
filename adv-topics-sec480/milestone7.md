# Deploying and Post Provisioning of BlueX Linux Servers

## 7.1 Create a Rocky 9.1 Base VM
- download minimal ISO from https://rockylinux.org/download
- install like a normal VM
- use https://raw.githubusercontent.com/gmcyber/RangeControl/main/src/scripts/base-vms/rhel-sealer.sh to sysprep the machine to create a base image


## 7.2 DHCP on fw-blue1 and a static (or dynamic) route on 480-fw

Create a static route on 480-fw such that 480-WAN traffic destined to the BLUE network IP space (10.0.5.0/24) is routed to the fw-blue1's eth0 interface
```
set protocols static route 10.0.5.0/24 next-hop 10.0.17.200
```


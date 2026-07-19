# Deploying and Post Provisioning of BlueX Linux Servers

## 7.1 Create a Rocky 9.1 Base VM
- download minimal ISO from https://rockylinux.org/download
- install like a normal VM
- use https://raw.githubusercontent.com/gmcyber/RangeControl/main/src/scripts/base-vms/rhel-sealer.sh to sysprep the machine to create a base image

adding new license from https://gist.github.com/Nyquist-CABJ/da70399eee8bdce0043858614ab22885

<img width="924" height="424" alt="image" src="https://github.com/user-attachments/assets/cb7ce381-e35b-43ba-a853-14adf3404ac4" />


## 7.2 DHCP on fw-blue1 and a static (or dynamic) route on 480-fw

Create a static route on 480-fw such that 480-WAN traffic destined to the BLUE network IP space (10.0.5.0/24) is routed to the fw-blue1's eth0 interface
```
set protocols static route 10.0.5.0/24 next-hop 10.0.17.200
```

### rocky configuration:
first, need to create deployer users on rocky systems
```
PS /home/charlotte/ChamplainTechJournals/adv-topics-sec480/ansible> ansible-playbook -i ./inventories/linux.yml ./create-deployer-user-rocky.yml -u root --ask-pass -K
```
then run playbook
```
PS /home/charlotte/ChamplainTechJournals/adv-topics-sec480/ansible> ansible-playbook -i ./inventories/linux.yml ./rocky-config.yml --ask-pass -K
```
it will take some time and machines will restart. then they will have new static IPs and deployer public key works


### ubuntu configuration
first, need to create deployer users on rocky systems
```
PS /home/charlotte/ChamplainTechJournals/adv-topics-sec480/ansible> ansible-playbook -i ./inventories/linux.yml ./create-deployer-user-ubuntu.yml -u root --ask-pass -K
```
then run playbook
```
PS /home/charlotte/ChamplainTechJournals/adv-topics-sec480/ansible> ansible-playbook -i ./inventories/linux.yml ./ubuntu-config.yml --ask-pass -K
```



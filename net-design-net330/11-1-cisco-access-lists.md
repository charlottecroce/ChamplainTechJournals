# 11-1 Cisco Access-List Assignment

<img width="1028" height="666" alt="{595D0742-75D0-4C15-97BE-AE9BA74F86BE}" src="https://github.com/user-attachments/assets/e3a968b0-4fec-4555-a00b-50fb01e4ebfb" />

Lab Goals:
### 1. Ping the various PCs and Servers to ensure connectivity
- as of now, all PCs and servers can ping each other
### 2.  Block the 192.168.11.0/24 network from entering (inbound serial 0/0/0) on Router 3 using a Standard ACL
```
ip access-list standard stnd-1
deny 192.168.11.0 0.0.0.255
permit any

int s0/0/0
R3(config-if)#ip access-group stnd-1 in
```

- PC3 (192.168.11.10) should not be able to ping PC5 (192.168.30.10)
- PC1 should be able to ping PC5

<img width="255" height="71" alt="{67EAF54A-83EB-450E-A55D-A5BD21E0AA93}" src="https://github.com/user-attachments/assets/2a25ff8e-511e-4333-a51a-b08ad24ab1f8" />


### 3. Block network 192.168.10.0/24 from reaching the Internet.

- On Router 2 serial 0/0/0, use an Extended ACL to prevent outbound packets from 192.168.10.0/24 from reaching the ISP address 200.200.200.1 
```
ip access-list extended extend-1
deny ip 192.168.10.0 0.0.0.255 200.200.200.1 0.0.0.0
permit ip any any

int s0/0/0
ip access-group extend-1 out
```

- PC1 should not be able to ping 200.200.200.1
- PC1 should be able to ping everything else

<img width="483" height="618" alt="{357F56D4-4847-4652-84A6-43BE1E47B94D}" src="https://github.com/user-attachments/assets/41f94920-9a33-47a6-8072-379b21d02af7" />


### 5. Complete 2  out of 3 Additional Configurations (listed as Bonus Tasks in .pka) using Extended Access Lists on the appropriate router

#### Configure the network to deny all access from the ISP to the File Server (192.168.20.210). Allow access from any other device.
```
ip access-list extended bonus-1
deny ip 200.200.200.0 0.0.0.255 192.168.20.210 0.0.0.0
permit ip any any

int f0/0
ip access-group bonus-1 out
```
<img width="261" height="93" alt="{00BC9669-BF7A-4305-8B3D-168675D06CF1}" src="https://github.com/user-attachments/assets/7f3ff30d-cc12-4ec7-8f34-9df6357ed207" />


#### Configure only Mail access to the Mail Server (192.168.20.200)
```
ip access-list extended bonus-2
permit tcp any 192.168.20.200 0.0.0.0 eq 25
deny ip any 192.168.20.200 0.0.0.0

int f0/0
ip access-group bonus-2 out
```
<img width="450" height="371" alt="{51857D6B-A40E-4705-A4AF-A291975AC7E8}" src="https://github.com/user-attachments/assets/4a0cbf18-521d-4326-840e-598693d5e58f" />

#### Configure only Web access to the Web Server (192.168.20.201)
```
ip access-list extended bonus-3
permit tcp any 192.168.20.201 0.0.0.0 eq 80
deny ip any 192.168.20.201 0.0.0.0

int f0/0
ip access-group bonus-3 out
```

<img width="608" height="333" alt="{89BD33F6-9B97-48CD-976B-86CBDAE3A37C}" src="https://github.com/user-attachments/assets/1af836cf-2696-48f6-bf77-7460739100ee" />
<img width="456" height="354" alt="{796F6A9D-B91C-4233-9EA9-3E368BB9F6BC}" src="https://github.com/user-attachments/assets/974059dd-12ee-409d-b8ca-23b9bd934261" />


Submission:

- Config of R1 showing the Bonus ACLs

<img width="559" height="324" alt="{A9D8D6CE-86B2-4B97-BCD8-37A96FB12DAD}" src="https://github.com/user-attachments/assets/65f40b29-15e9-41c4-b5f5-2b307ec5bfab" />


- Showing results from "Check Results", You should have green check marks for everything except the VTY settings


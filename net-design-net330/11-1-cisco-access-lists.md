# 11-1 Cisco Access-List Assignment

<img width="1028" height="666" alt="{595D0742-75D0-4C15-97BE-AE9BA74F86BE}" src="https://github.com/user-attachments/assets/e3a968b0-4fec-4555-a00b-50fb01e4ebfb" />

Lab Goals:
1. Ping the various PCs and Servers to ensure connectivity
2.  Block the 192.168.11.0/24 network from entering (inbound serial 0/0/0) on Router 3 using a Standard ACL

Rr is a typo - should be R2
PC3 (192.168.11.10) should not be able to ping PC5 (192.168.30.10
PC1 should be able to ping PC5
3. Block network 192.168.10.0/24 from reaching the Internet.

On Router 2 serial 0/0/0, use an Extended ACL to prevent outbound packets from 192.168.10.0/24 from reaching the ISP address 200.200.200.1 

PC1 should not be able to ping 200.200.200.1

PC1 should be able to ping everything else

4. Skip VTY exercise

5. Complete 2  out of 3 Additional Configurations (listed as Bonus Tasks in .pka) using Extended Access Lists on the appropriate router

ISP Network is 200.200.200.0/24
Web is TCP port 80
ping should fail to browser from PC's
To test Web, you can use the PC Desktop "Web Browser" and go to 192.168.20.201
Mail is TCP port 25
To test Mail access from a PC:
go to the PC command line
Telnet 192.168.20.200 25
Will show "Trying 192.168.20.200...Open" if port is open
Ctrl and the "]" key will cancel telnet
Submission:

Screenshots With Your Name or other Identifier present-
Showing results from "Check Results", You should have green check marks for everything except the VTY settings
Example (see my name in the PT path) - If needed, you can add your name by opening a text editor or command prompt and typing your name so it is in the screenshot

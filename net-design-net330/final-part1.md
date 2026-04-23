# NET 330 - Final Design Project Part 1

For this final project, you will design a network for a hospital with a main campus and two remote community hospitals. 

You will also create an emulation of that network in Packet Tracer with a working configuration.

IT IS ONLY NECESSARY TO IMPLEMENT THE MAIN CAMPUS

## Scenario:
You have been contracted to design a network for a new medical center.  You have been provided with the following information:

### Facilities:

- Main Campus Hospital:  
  - 3 buildings, East, Central, and West
  - Each of the 3 buildings has a distribution switch/router
  - The Data Center is in Central
  - A Border router on Central connects Main Campus to the Internet/ISP
  - A Core Switch in Central connects the Main Campus Distribution Routers and the Main Campus Border Router
- Community Hospital South
  - 1 Building
  - Has one multi-layer switch acting as a border and distribution router
  - Has edge switches
- Community Hospital North
  - 1 Building
  - Has one multi-layer switch acting as a border and distribution router
  - Has edge switches

<img width="1396" height="856" alt="image" src="https://github.com/user-attachments/assets/fb0a6aef-2fc8-44e7-ae02-303d5e2da97e" />

### VLANs/IP Addressing

The Hospital organization is assigned the following public IP networks used to connect to the ISP

- Main: 152.16.10.0/24
- South: 212.232.16.0/24
- North: 89.25.202.0/24

The Private Addressing space of 172.16.0.0/16 will be used for all internal VLANs.

- Main Campus VLANs
  - All internal VLANs use Private Addressing
  - A Backbone VLAN for the Distribution Routers (150 IPs)
  - A clinic vlan  trunked between buildings (need 600 IP's)
  - A guest vlan trunked between buildings (need 600 IP's)
  - A shared (trunked) vlan for building controls in each building (need 400 IP's)
  - A Psych vlan in East (150 IPs - East Distribution Router is the Gateway)
  - A Counseling vlan in West (150 IPs - West Disctribution Router is the Gateway)
  - Data Center VLANs in Central 
    - Production Servers (150 IPs)
    - Development Servers (150 IPs)
    - Health Record Servers (150 IPs)
  - NOTE: Central Distribution Router is the Gateway for all VLANs except Psych (East) and Counseling (West)
- South VLANs
  - All internal VLANs use Private Addressing
  - A clinic vlan (150 IPs)
  - A guest vlan (150 IPs)
  - A building control vlan (150 IPs)
- North VLANs
  - All internal VLANs use Private Addressing
  - A clinic vlan (150 IPs)
  - A guest vlan (150 IPs)
  - A building control vlan (150 IPs)

## Assignment for Part 1:

1. Create a Subnet/VLAN table for all internal networks in Main (East, West, Central), South, and North that includes:
  - VLAN ID
  - VLAN Name
  - Network Address
  - Subnet Mask
  - Default Gateway
  - Submit Table
2. Create a network design in Packet Tracer that includes:
  - Main Campus (all 3 buildings/Distribution Areas), North, South
  - Main Campus Border Router(Cisco 2911)
  - Main Campus Distribution Routers/Switches (Cisco 3560 Multi-Layer Switch)
  - Main Campus Core Switch (Cisco 2960)
  - North and South combined Border/Distribution Router (Cisco 3560 Multi-Layer Switch)
  - Edge switches (Cisco 2960)
    - 1 each in West-Main, East-Main, North, and South
    - 2 in Central-Main: 1 for the building users, and 1 for the Data Center
- ISP Router (Cisco 2911)

When complete, your network should look something like this (note that the ISP router is missing from the image):

<img width="874" height="645" alt="image" src="https://github.com/user-attachments/assets/8259092a-a3d4-432d-a38d-fe32baffda7e" />


Connect devices with cables as required
Configure IP address
For routers
IP addresses on physical interfaces 
For Multi-layer Switches (aka routing switches)
VLAN definitions (what VLANs will be on that switch)
Don't forget the Backbone VLAN for Central Campus Routers
IP address on the VLAN interfaces
NOTE: Remember, every IP address can only be used once.  For router to router connections, make sure each side has a unique IP
On the switches configure VLANS
On Edge Switches
Define VLANs
Create some Access Ports for each VLAN
Configure trunk ports for the port connecting to the Distribution Router
On Core Switch
Define VLANs
Configure Trunk Ports as required
On Multi-Layer Switches
Configure Trunk Ports as required
Main Campus OSPF
Configure OSPF on the Main Campus routers (we will address North and South in Part 2)
Use OSPF authentication
Add workstations to:
Psych VLAN (East)
Counseling VLAN (West)
Clinic VLAN (Central)
Clinic VLAN (West)
Production Server VLAN (Central)
Assign IP addresses from the VLAN to those workstations
Confirm OSPF is working by pinging between VLANs
NOTE: "sh ip route" will show you the routing tables on the distribution routers.  
Submit working Packet Tracer File
Submission:

Subnet Table
Packet Tracer File

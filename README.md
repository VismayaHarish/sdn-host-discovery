# SDN Host Discovery using POX and Mininet

## Problem Statement
This project implements a Host Discovery Service in Software Defined Networking (SDN) using a POX controller. The goal is to dynamically detect hosts in the network and maintain their information, including MAC address, switch ID, and port number.

## Tools Used
* Mininet
* POX Controller
* OpenFlow
* Ubuntu (Virtual Machine)
  
## Features
* Dynamically detects hosts connected to the network
* Maintains host information (MAC address, switch, port)
* Implements basic learning switch functionality
* Installs flow rules using OpenFlow
* Handles packet_in events from switches
* Performs packet forwarding using flooding

## How It Works
When a switch receives a packet that does not match any existing flow rule, it sends the packet to the controller as a packet_in event. The controller extracts the source MAC address and records the host’s location (switch ID and port). It then installs appropriate flow rules so that future packets can be forwarded efficiently without involving the controller.

## Execution Steps

### Step 1: Start the POX Controller
'''bash
cd ~/pox
./pox.py host_discovery
'''

### Step 2: Start Mininet with Remote Controller
'''bash
sudo mn --controller=remote,ip=127.0.0.1,port=6633
'''

### Step 3: Test Connectivity
'''bash
pingall
'''

## Screenshots
- Mininet pingall output (0% packet loss)
- Controller logs showing host discovery

## Output
* Successful communication between hosts (0% packet loss)
* Hosts are detected dynamically and displayed in the controller logs

## Author
Vismaya Harish

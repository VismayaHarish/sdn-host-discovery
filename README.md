# SDN Host Discovery using Ryu and Mininet

## Problem Statement
This project implements a Host Discovery Service in Software Defined Networking (SDN) using a Ryu controller. The goal is to dynamically detect hosts in the network and maintain their information, including MAC address, switch ID, and port number.

## Tools Used
* Mininet
* Ryu Controller
* OpenFlow 1.3
* Ubuntu (WSL)
* 
## Features
* Dynamically detects hosts connected to the network
* Maintains host information (MAC address, switch, port)
* Implements basic learning switch functionality
* Installs flow rules using OpenFlow
* Handles packet_in events from switches

## How It Works
When a switch receives a packet that does not match any existing flow rule, it sends the packet to the controller as a packet_in event. The controller extracts the source MAC address and records the host’s location (switch ID and port). It then installs appropriate flow rules so that future packets can be forwarded efficiently without involving the controller.

## Execution Steps

### Step 1: Start the Ryu Controller
cd ~/ryu
export PYTHONPATH=$PWD
python3 ryu/cmd/manager.py host_discovery.py

### Step 2: Start Mininet
sudo mn --topo single,3 --controller none --switch ovs,protocols=OpenFlow13

### Step 3: Connect the Switch to the Controller
sh ovs-vsctl set-controller s1 tcp:127.0.0.1:6633

### Step 4: Test Connectivity
pingall

## Output
* Successful communication between hosts (0% packet loss)
* Hosts are detected dynamically and displayed in the controller logs

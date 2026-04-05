# SDN Host Discovery

This project implements a Host Discovery Service using Ryu controller and Mininet.

## Features
- Detects hosts dynamically
- Uses OpenFlow 1.3
- Implements learning switch

## Run
1. Start controller:
   python3 ryu/cmd/manager.py host_discovery.py

2. Start Mininet:
   sudo mn --topo single,3 --controller none --switch ovs,protocols=OpenFlow13

3. Connect:
   sh ovs-vsctl set-controller s1 tcp:127.0.0.1:6633

4. Test:
   pingall

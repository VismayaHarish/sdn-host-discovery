# SDN Host Discovery using Ryu and Mininet

## 📌 Problem Statement
This project implements a Host Discovery Service in Software Defined Networking (SDN) using a Ryu controller. The controller dynamically detects hosts and maintains their information.

---

## 🛠 Tools Used
- Mininet
- Ryu Controller
- OpenFlow 1.3
- Ubuntu (WSL)

---

## ⚙️ Features
- Detects hosts dynamically
- Displays MAC address, switch ID, and port
- Implements learning switch logic
- Installs flow rules dynamically

---

## 🧠 How It Works
- Switch sends unknown packets to controller (packet_in)
- Controller extracts MAC address from packets
- Stores host information (MAC, switch, port)
- Installs flow rules for efficient forwarding

---

## ▶️ Execution Steps

### 1. Start Ryu Controller
```bash
cd ~/ryu
export PYTHONPATH=$PWD
python3 ryu/cmd/manager.py host_discovery.py

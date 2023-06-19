# WIFI Network Scanner

The script can be run to monitor the network for new devices continuously. By executing this code, you can leverage **Scapy**'s functionality to detect and retrieve the IP and MAC addresses of devices that join your network in real-time.

# Scapy

Scapy is a powerful Python library that allows for the creation, manipulation, and sending of network packets. It provides a flexible and intuitive interface for network packet crafting, packet sniffing, network scanning, and network discovery. 

Scapy enables developers to work at a low-level network protocol layer, giving them control over packet fields and headers.

# ARP
ARP (Address Resolution Protocol) is a protocol used in computer networks to map IP addresses to MAC addresses. IP addresses are logical addresses used by computers to identify each other, while MAC addresses are physical addresses assigned to network interfaces. When devices need to communicate, they rely on MAC addresses for proper data transmission. 

To find the MAC address associated with a specific IP address, a device sends an ARP request to the network, asking which device has that IP address. The device with the matching IP address responds with its MAC address. Once the requesting device receives this response, it can use the MAC address to direct the packet to the correct recipient.

ARP is essential for devices to communicate effectively on a network, enabling the translation between IP addresses and MAC addresses.
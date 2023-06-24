from scapy.all import ARP, Ether, srp
import time

# Creating ARP request , sending it  and receiving the results
def detect_new_devices():
    known_devices = {}
    target_ip = "192.168.1.1/24"
    
    # Send an ARP request to all devices in the network
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]

    # Process the response and detect new devices
    for sent, received in result:
        device_ip = received.psrc
        device_mac = received.hwsrc
        known_devices[device_ip] = device_mac

    return known_devices

# Printing all the IP and MAC 
def show(kd):
    keys = list(kd.keys())
    for key in keys :
        print("Connected device: IP = {}, MAC = {}".format(key,kd[key]))
    print("-------------------")

# Show how many devices are connected 
def count(kd):
    le = len(kd)
    print("There are {} conected ".format(le))
    
# Main
if __name__ == "__main__":
    while True:
        try:
            kd = detect_new_devices()
            show(kd)
            #count(kd)
            time.sleep(5)
        
        except KeyboardInterrupt:
            print("Monitoring stopped.")
            break

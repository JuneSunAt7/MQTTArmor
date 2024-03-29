from scapy.all import *


def discover_mqtt_devices():
    devices = set()

    def packet_callback(packet):
        if packet.haslayer(TCP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            if dst_port == 1883:
                devices.add(dst_ip)

    sniff(prn=packet_callback, filter="tcp", store=0)

    return devices

def finder():
    mqtt_devices = discover_mqtt_devices()

    if not mqtt_devices:
        print("MQTT devices not found in the local network")
    else:
        print("Found MQTT devices in the local network:")
        for device in mqtt_devices:
            print(device)

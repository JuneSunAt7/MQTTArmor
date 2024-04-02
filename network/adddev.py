from scapy.all import *
from logger.printer import *

def find_mqtt_devices():
    # Отправляем ARP запрос для получения списка устройств в сети
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.0/24"), timeout=2, verbose=0)

    mqtt_devices = []

    for _, rcv in ans:
        if rcv.haslayer(IP):
            ip = rcv[ARP].psrc
            # Отправляем MQTT запрос к устройству
            response = sr1(IP(dst=ip) / TCP(dport=1883, flags="S"), timeout=1, verbose=0)
            if response and response.haslayer(TCP) and response[TCP].sport == 1883:
                mqtt_devices.append(ip)

    return mqtt_devices


if __name__ == "__main__":
    mqtt_devices = find_mqtt_devices()
    logs = Logger()
    if len(mqtt_devices) == 0:

        logs.warning("No devices")
    else:
        print("MQTT devices:")
        for device in mqtt_devices:
            logs.succes(device)

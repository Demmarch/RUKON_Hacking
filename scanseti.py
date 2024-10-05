import time
from scapy.all import sniff, IP
def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        print("Protocol: IPv4")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol Number: {proto}")
        print("=" * 50)


# Запрос ввода имени сетевого интерфейса
interface = input("Введите имя сетевого интерфейса: ")

# Захват трафика в течение 30 секунд
timeout = 30  # Время в секундах
print(f"Захват трафика на интерфейсе {interface} в течение {timeout} секунд...")

packets = sniff(iface=interface, timeout=timeout, prn=analyze_packet)

print(f"Захват трафика завершен. Захвачено {len(packets)} пакетов.")
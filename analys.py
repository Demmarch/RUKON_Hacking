from scapy.all import *
def packet_handler(pkt):
    if IP in pkt:
        source_ip = pkt[IP].src
        dest_ip = pkt[IP].dst
        if TCP in pkt:
            source_port = pkt[TCP].sport
            dest_port = pkt[TCP].dport
            protocol = "TCP"
        elif UDP in pkt:
            source_port = pkt[UDP].sport
            dest_port = pkt[UDP].dport
            protocol = "UDP"
        else:
            source_port = "N/A"
            dest_port = "N/A"
            protocol = "Other"
        print(f"Protocol: {protocol}")
        print(f"Source IP: {source_ip}, Source Port: {source_port}")
        print(f"Dest IP: {dest_ip}, Dest Port: {dest_port}")
        print("=" * 30)
# Захватываем сетевой трафик с интерфейса 'en0' (замените на свой интерфейс)
sniff(iface='Беспроводная сеть', prn=packet_handler)
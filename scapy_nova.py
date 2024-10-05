from scapy.all import *

def analyze_traffic(interface):
    print("Анализ сетевого трафика на интефейсе", interface)
    sniff(filter="arp", iface=interface, prn=lambda x: x.summary())


if __name__ == "__main__":
    interface = "Беспроводная сеть"
    analyze_traffic(interface)
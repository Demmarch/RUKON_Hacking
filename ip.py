# import socket
#
# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)
# print(ip)

import requests
import socket

def scan_ports(target_ip, ip_port):
    open_ports = []
    for por in range(ip_port[0], ip_port[1]+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.07)
        result = sock.connect_ex((target_ip, por))
        if result==0:
            open_ports.append(por)
            print(por)
        sock.close()
    return open_ports

def main():
    respo = requests.get("https://api64.ipify.org")
    public_ip = respo.text
    print(public_ip)
    target_ip = input("IP адрес для сканирования ")
    staart_port = int(input("Введите начальный порт "))
    end_port = int(input("Введите конечный порт "))
    port_range = (staart_port, end_port)
    open_ports = scan_ports(public_ip, port_range)
    if len(open_ports) > 0:
        print("Открытые порты:")
        for port in open_ports:
            print(f"Порт {port} открыт")
    else:
        print("Нет открытых портов")

if __name__ == "__main__":
    main()

from scapy.all import *
def scan_network(target_ip, start_port, end_port):
    open_ports = []
    # Итерация по диапазону портов и отправка пакетов
    for port in range(start_port, end_port + 1):
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        # Отправка пакета и получение ответа
        response = sr1(packet, timeout=2)
        # Анализ полученного ответа и определение открытых портов
        if response is not None:
            if response.haslayer(TCP) and response[TCP].flags == "SA":
                open_ports.append(port)
    return open_ports

def recomendation(open_ports):
    recomendations = {}
    for port in open_ports:
        if port == 21:
            recomendations[port] = "Обеспечьте безопастность FTP сервера"
        elif port == 22:
            recomendations[port] = "Закройте ненужный SSH порт"
        elif port == 23:
            recomendations[port] = "Закройте ненужный TelNet порт"
        elif port > 23 and port < 80:
            recomendations[port] = f"Проверьте необходимость доступа в порта {port}. Возможно нужно закрыть"
        elif port == 80:
            recomendations[port] = "Обеспечьте безопасность web сервера"
        elif port > 80 and port < 443:
            recomendations[port] = f"Проверьте необходимость доступа в порт {port}. Возможно надо закрыть"
        elif port == 443:
            recomendations[port] = "Обеспечьте безопасность web сервера"
        elif port > 443 and port < 1443:
            recomendations[port]=f"Проверьте необходимость доступа в порт {port}. Наверное надо закрыть"
        elif port ==1443:
            recomendations[port]=f"Проверьте VPN"
        else:
            recomendations[port]=f"Проверьте необходимость доступа в порт {port}. Наверное надо закрыть"
    return recomendations


# Запрос ввода IP-адреса для сканирования
target_ip = input("Введите IP-адрес для сканирования: ")
start_port = int(input("Введите начальный порт: "))
end_port = int(input("Введите конечный порт: "))
# Запуск сканирования
open_ports = scan_network(target_ip, start_port, end_port)
# Вывод результатов сканирования
if len(open_ports) > 0:
    print("Открытые порты на устройстве с IP-адресом {}: ".format(target_ip))
    recomendations = recomendation(open_ports)
    for port in open_ports:
        print("- Порт {}".format(port))
        print(f"Рекомендация: {recomendations.get(port)}")
else:
    print("Не обнаружено открытых портов на устройстве с IP-адресом{}".format(target_ip))
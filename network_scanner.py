import ipaddress
from ping3 import ping


def scan_network(ip_range):
    active_hosts = []
    try:
        # Разбиваем IP-диапазон на объекты ipaddress.IPv4Address
        network = ipaddress.ip_network(ip_range)
        for ip in network.hosts():
            ip_str = str(ip)
            response_time = ping(ip_str, timeout=1) # Посылаем ping иполучаем время ответа
            if response_time is not None and response_time is not False:
                active_hosts.append(ip_str)
    except Exception as scan_exception:
        print(f"Произошла ошибка при сканировании: {scan_exception}")
    return active_hosts


if __name__ == "__main__":
    try:
        # Введите IP-диапазон, который вы хотите сканировать например, "192.168.1.0/24":)
        input_ip_range = input("Введите IP-диапазон для сканирования(в формате CIDR): ")
        active_hosts = []
        try:
            active_hosts = scan_network(input_ip_range)
        except Exception as e:
            print(f"Произошла ошибка при сканировании: {e}")
        if active_hosts:
            print("Активные устройства в сети:")
            for host in active_hosts:
                print(host)
        else:
            print("Активные устройства не обнаружены.")
    except KeyboardInterrupt:
        print("\nСканирование прервано пользователем.")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")
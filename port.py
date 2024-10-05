import socket
def is_port_in_use(port):
    # Создаем сокет для проверки порта
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            # Привязываем сокс к указанному порту
            s.bind(("127.0.0.1", port))
        except OSError:
            # Если порт занят, возвращаем True
            return True
            # Если порт свободен, возвращаем False
    return False

def main():
    try:
        # Запрашиваем у пользователя порт для проверки
        port_start = int(input("Введите начальный порт: "))
        port_end = int(input("Введите конечный порт: "))
        for port in range(port_start, port_end+1):
            if is_port_in_use(port):
                print(f"Порт {port} занят")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое числопорта.        ")
if __name__ == "__main__":
    main()
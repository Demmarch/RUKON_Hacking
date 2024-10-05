import socket
# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Указываем IP адрес и порт сервера
server_address = ('localhost', 12345)
# Привязываем сокет к адресу и порту
server_socket.bind(server_address)
# Начинаем слушать входящие подключения
server_socket.listen(1)
print("Ждем подключения клиента...")
while True:
    # Принимаем подключение
    client_socket, client_address = server_socket.accept()
    print(f"Подключен клиент с адресом {client_address}")
    try:
        while True:
            # Читаем данные от клиента
            data = client_socket.recv(1024)
            print(f"Получено от клиента: {data.decode()}")
            # Отправляем ответ клиенту
            response = "Привет, клиент!"
            client_socket.sendall(response.encode())
    finally:
        # Закрываем сокет клиента
        client_socket.close()
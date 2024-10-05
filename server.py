import socket
# IP адрес и порт сервера
server_ip = '127.0.0.1' # Или 'localhost' для локального тестирования
server_port = 8080
# Создаем сокет и привязываем его к адресу и порту
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
# Начинаем прослушивать входящие соединения
server_socket.listen(1)
print(f"Сервер слушает на {server_ip}:{server_port}...")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Подключен клиент с адресом {client_address}")
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Получено от клиента: {data}")
        # Отправляем обратно клиенту ответ
        response = input("Введите ответ для клиента: ")
        client_socket.send(response.encode())
    client_socket.close()
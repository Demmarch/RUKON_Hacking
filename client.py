import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Указываем IP адрес и порт сервера
server_address = ('localhost', 12345)
# Подключаемся к серверу
client_socket.connect(server_address)
try:
    # Отправляем данные на сервер
    message = "Heloo server!"
    while True:
        message = input()
        client_socket.sendall(message.encode())
        # Ждем ответ от сервера
        data = client_socket.recv(1024)
        print(f"Получен ответ от сервера: {data.decode()}")
finally:
    # Закрываем сокет
    client_socket.close()
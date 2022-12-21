import socket

# SERVER address (к которому будем подключаться)
host = '127.0.0.1'
port = 65400

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as service:
    service.connect((host, port))  # устанавливаем соединение
    while True:
        message = input()
        message = message.encode('utf-8') + b'\x00'
        service.sendall(message)

        response = service.recv(8)
        print(response.decode('utf-8'))

import socket

server_host = '127.0.0.1'
server_port = 65333

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((server_host, server_port))
    # устанавливает соединение с этим адресом
    while True:
        s = input()
        client.sendall(s.encode('utf-8'))
        # bytes.decode преобразует байты в строку
        # str.encode кодирует строку байтами
        response = client.recv(2)
        print(response.decode('utf-8'))

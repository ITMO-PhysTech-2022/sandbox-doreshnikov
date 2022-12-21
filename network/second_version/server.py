import socket

MAX_PORT = 65535

host = '127.0.0.1'
port = 65333

# socket - класс, описывающий соединение через какой-то адрес
# AF_INET - указание, что будем использовать IPv4 адрес
# SOCK_STREAM - указание, что используем TCP
# альтернативный вариант - SOCK_DGRAM - использовать UDP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((host, port))  # резервирует этот адрес за нами
    '''
    server <- message -- client
    server печает message
    server -- OK ->      client
    '''
    server.listen()
    conn, addr = server.accept()
    # conn отвечает за взаимодействие с подключенным клиентом
    # addr - адрес клиента
    print(f'Client connected from {addr}')

    with conn:
        while True:
            def receive_one_message():
                data = b''
                while True:
                    new_data = conn.recv(20)
                    data += new_data
                    if len(new_data) < 20:
                        break
                return data.decode('utf-8')

            # data = conn.recv(20)  # recv = receive
            # print(data.decode('utf-8'))
            # data - массив байт, преобразовать в строку = .decode()
            message = receive_one_message()
            print(message)
            conn.sendall(b'Ok')

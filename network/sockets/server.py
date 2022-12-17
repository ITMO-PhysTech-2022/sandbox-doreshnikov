import socket

host = '127.0.0.1'  # localhost
port = 65400

'''
f = open('name')
f.write(...)
f.close()

with open('name') as f:
    f.write(...)
'''

# SOCK_STEAM = TCP
# SOCK_DGRAM = UDP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as service:
    service.bind((host, port))  # запустить сервис на этом адресе
    service.listen()
    conn, addr = service.accept()
    print(f'Connected from address {addr}')

    with conn:
        # Hello, World!
        # Hello, World!\x00

        def receive():
            data = b''
            while True:
                new_data = conn.recv(8)  # receive
                data += new_data
                if b'\x00' in new_data:
                    data = data[:data.find(b'\x00')]
                    break
            return data.decode('utf-8')

        while True:
            message = receive()
            print(message)
            conn.sendall(b'Ok...')
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from time import strftime, localtime

host = gethostbyname('localhost')
port = 9090
clients = []

server = socket(AF_INET, SOCK_DGRAM)
server.bind((host, port))

_exit = False
print('Server started')
print(f'{host}:{port}')
while not _exit:
    try:
        data, addr = server.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        set_time = strftime("%d.%m.%Y %H:%M", localtime())
        print(f'{addr[0]}:{addr[1]} -> {set_time}')
        print(data.decode('utf-8'))
        for client in clients:
            if client != addr:
                server.sendto(data, client)

    except RuntimeError:
        print('Server stopped')
        _exit = True
server.close()
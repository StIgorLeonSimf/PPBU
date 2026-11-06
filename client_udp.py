from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from threading import Thread
from time import sleep

_exit = False
_join = False


def receive(name, sock):
    while not _exit:
        try:
            while True:
                data, address = sock.recvfrom(1024)
                print(data.decode('utf-8'))
                sleep(.2)
        except RuntimeError:
            print(f'Receiving {name} failed')
            break


host = gethostbyname('localhost')
port = 0

server = ('127.0.0.1', 9090)
client = socket(AF_INET, SOCK_DGRAM)
client.bind((host, port))
client.setblocking(True)
alias = input('Your name: ')
thread = Thread(target=receive, args=(alias, client))
thread.start()
while _exit is False:
    if _join is False:
        client.sendto(f'{alias} -> join to chat'
                      .encode('utf-8'), server)
        _join = True
    else:
        try:
            message = input('Your message: ')
            if message != '':
                client.sendto(f'[{alias}]{message}'.encode('utf-8'), server)
            sleep(.2)
        except RuntimeError:
            client.sendto(f'[{alias}] -> left chat'.encode('utf-8'), server)
            _exit = True
thread.join()
client.close()
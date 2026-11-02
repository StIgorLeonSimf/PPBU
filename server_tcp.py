import socket

#1 параметры подключения
ip = '127.0.0.1'
port = 9001
end_point = (ip, port)

# сокет сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(end_point)

server.listen(10)

# режим ожидания запросов
print(f'Сервер запущен на IP-{ip}:{port}')
print('Ожидание запроса на соединение')
connection, client_address = server.accept()

#Обмен данными с клиентом
try:
    print(f'Установлено соединение с клиентом: {client_address}')
    while True:
        #принимаем сообщение
        client_message = connection.recv(1024).decode(encoding='utf-8')
        if not client_message or client_message == 'stop_server':
            break
        print(f'Сообщение от клиента: [{client_message}]')
        # отправка сообщения
        server_message = input('Ответ сервера: ')
        connection.send(server_message.encode(encoding='utf-8'))
        print('Сообщение отправлено!')

except BaseException as e:
    print(e)
finally:
    connection.close()
    print('Сервер остановлен')

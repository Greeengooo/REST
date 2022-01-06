if __name__ == '__main__':
    import socket

    sock = socket.socket()
    sock.bind(('127.0.0.1', 8888))
    sock.listen(1)
    conn, addr = sock.accept()

    print('Соединение установлено:', addr)

    # переменная response хранит строку возвращаемую сервером, если вам для
    # тестирования клиента необходим другой ответ, измените ее
    response = b'ok\npalm.cpu 8.3 1501864340\npalm.cpu 10.5 1501864247\n\n'
    #response = b'error\nwrong command\n\n'
    #response = b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\npalm.cpu 8.3 1501864340\neardrum.memory 200 1501861111\n\n'
    #response = b'ok\npalm.cpu not_value 1501864247\npalm.cpu 8.3 1501864340\n\n'
    #response = b'ok\nblablabla\n\n'
    #response = b'ok\n\n'
    #response = b'ok\neardrum.memory 200 1501861111\n\n'
    #response = b'ok\npalm.cpu 10.5 1501864247\nok\n\n'
    #response = b'blablabla\nok\n\n'

    while True:
        data = conn.recv(1024)
        if not data:
            break
        request = data.decode('utf-8')
        print(f'Получен запрос: {ascii(request)}')
        print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
        conn.send(response)

    conn.close()
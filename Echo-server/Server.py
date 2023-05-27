import socket
import threading
import logging


def handle_client(client_socket, client_address):
    logging.basicConfig(filename='server.log', level=logging.INFO)

    logging.info(f'Подключение клиента: {client_address}')

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            client_socket.send(data)

            logging.info(f'Прием данных от клиента: {data.decode()}')
            logging.info(f'Отправка данных клиенту: {data.decode()}')

        except ConnectionResetError:
            break

    client_socket.close()

    logging.info(f'Отключение клиента: {client_address}')


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = input("Введите номер порта (по умолчанию 12345): ") or 12345
port = int(port)

while True:
    try:
        server_socket.bind(('localhost', port))
        break
    except OSError:
        port += 1

print(f'Сервер запущен и слушает порт: {port}')

server_socket.listen(5)
print('Начало прослушивания порта')

while True:
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

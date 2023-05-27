import socket
import logging

def send_message(client_socket, message):
    message_length = len(message)

    header = str(message_length).ljust(10)
    client_socket.send(header.encode())

    client_socket.send(message.encode())

def receive_message(client_socket):
    header = client_socket.recv(10).decode().strip()

    if header:
        message_length = int(header)
        message = client_socket.recv(message_length).decode()
        return message

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Введите имя хоста (по умолчанию localhost): ") or 'localhost'
port = input("Введите номер порта (по умолчанию 12345): ") or 12345
port = int(port)

client_socket.connect((host, port))
print(f'Соединение с сервером {host}:{port}')

while True:
    message = input('Введите сообщение (exit для выхода): ')

    send_message(client_socket, message)

    if message.lower() == 'exit':
        break

    response = receive_message(client_socket)
    print('Прием данных от сервера:', response)

client_socket.close()
print('Разрыв соединения с сервером')

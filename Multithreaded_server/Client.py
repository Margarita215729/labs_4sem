import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except Exception as e:
            print(f"Ошибка при получении сообщения: {e}")
            break

def send_messages(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())

def start_chat_client():
    host = '127.0.0.1'
    port = 54321

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    username = input("Введите имя пользователя: ")
    client_socket.send(username.encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

start_chat_client()

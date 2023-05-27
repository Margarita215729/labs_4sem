import socket
import threading
import time

class MessageHistory:
    def __init__(self, max_messages=10):
        self.max_messages = max_messages
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def get_messages(self):
        return self.messages

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = None
        self.clients = []
        self.history = MessageHistory()

        self.is_running = True
        self.is_paused = False

        self.control_thread = threading.Thread(target=self.process_commands)
        self.control_thread.start()

    def start(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)

        print(f"Сервер запущен на {self.host}:{self.port}")

        while self.is_running:
            if self.is_paused:
                time.sleep(1)
                continue

            conn, addr = self.server.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            client_thread.start()

    def handle_client(self, conn, addr):
        username = conn.recv(1024).decode()
        self.send_message_to_all(f"{username} присоединился к чату.")
        self.clients.append((conn, username))

        self.send_message_history(conn)

        while self.is_running:
            if self.is_paused:
                time.sleep(1)
                continue

            try:
                data = conn.recv(1024)
                if data:
                    message = data.decode()
                    self.send_message_to_all(f"{username}: {message}")
                    self.history.add_message(f"{username}: {message}")
                else:
                    break
            except Exception as e:
                print(f"Ошибка при обработке сообщения от {username}: {e}")
                break

        self.clients.remove((conn, username))
        self.send_message_to_all(f"{username} покинул чат.")
        conn.close()

    def send_message_to_all(self, message):
        for client in self.clients:
            conn, _ = client
            try:
                conn.sendall(message.encode())
            except Exception as e:
                print(f"Ошибка при отправке сообщения: {e}")

    def send_message_history(self, conn):
        messages = self.history.get_messages()
        if messages:
            conn.send("\n".join(messages).encode())

    def process_commands(self):
        while self.is_running:
            command = input("Введите команду ('stop', 'pause', 'logs', 'clear_logs', 'clear_auth'): ")
            if command == "stop":
                self.stop()
            elif command == "pause":
                self.pause()
            elif command == "logs":
                self.show_logs()
            elif command == "clear_logs":
                self.clear_logs()
            elif command == "clear_auth":
                self.clear_authentication()
            else:
                print("Неверная команда. Повторите ввод.")

    def stop(self):
        self.is_running = False
        self.is_paused = False
        self.server.close()
        print("Сервер остановлен.")

    def pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            print("Сервер приостановлен.")
        else:
            print("Сервер возобновлен.")

    def show_logs(self):
        messages = self.history.get_messages()
        if messages:
            print("\n".join(messages))
        else:
            print("Нет доступной истории сообщений.")

    def clear_logs(self):
        self.history = MessageHistory()
        print("История сообщений очищена.")

    def clear_authentication(self):
        with open("auth.txt", "w") as f:
            f.write("")
        print("Файл идентификации очищен.")


chat_server = ChatServer('127.0.0.1', 54321)
chat_server.start()

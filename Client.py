import socket

def start_client():
    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Клиент: сокет создан")

    # Подключаемся к серверу
    server_address = ('localhost', 9090)
    client_socket.connect(server_address)
    print(f"Клиент: подключение к серверу {server_address}")

    try:
        # Считываем строку со стандартного ввода
        message = input("Введите сообщение для отправки серверу: ")

        # Отправляем данные серверу
        client_socket.sendall(message.encode())
        print(f"Клиент: данные отправлены серверу: {message}")

        # Принимаем данные от сервера
        data = client_socket.recv(1024)
        print(f"Клиент: данные получены от сервера: {data.decode()}")
    except Exception as e:
        print(f"Клиент: произошла ошибка: {e}")
    finally:
        client_socket.close()
        print("Клиент: соединение закрыто")

if __name__ == "__main__":
    start_client()

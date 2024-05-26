import socket

def start_server():
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Сервер: сокет создан")

    # Связываем сокет с хостом и портом
    host = ''
    port = 9090
    server_socket.bind((host, port))
    print(f"Сервер: сокет привязан к {port}")

    # Начинаем прослушивание порта
    server_socket.listen(1)
    print(f"Сервер: прослушивание порта {port}")

    # Принимаем подключение клиента
    conn, addr = server_socket.accept()
    print(f"Сервер: подключение клиента {addr}")

    try:
        while True:
            # Принимаем данные от клиента порциями по 1024 байта
            data = conn.recv(1024)
            if not data:
                print("Сервер: данные от клиента не получены, отключение клиента")
                break
            print(f"Сервер: данные получены от клиента: {data.decode()}")

            # Отправляем данные обратно клиенту (Эхо)
            conn.send(data)
            print(f"Сервер: данные отправлены клиенту: {data.decode()}")
    except Exception as e:
        print(f"Сервер: произошла ошибка: {e}")
    finally:
        conn.close()
        print("Сервер: соединение закрыто")

    server_socket.close()
    print("Сервер: остановлен")

if __name__ == "__main__":
    start_server()

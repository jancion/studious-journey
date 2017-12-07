import socket

HOST = ''
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_socket:
    listening_socket.bind((HOST, PORT))
    listening_socket.listen(1)
    conn, addr = listening_socket.accept()
    with conn:
        print("Connection from", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received", data)
            conn.sendall(data)



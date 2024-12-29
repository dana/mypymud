#!/usr/local/bin/python3

import socket

client_sockets = []

def start_server():
    host = '0.0.0.0'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((host, port))

    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        client_socket.send("Connected to server\n".encode())

        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

        message = "Hello from the server!"
        client_socket.send(message.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()


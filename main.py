#!/usr/local/bin/python3

import socket

def start_server():
    host = '0.0.0.0'
    port = 5000

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive data from the client
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

        # Send a response to the client
        message = "Hello from the server!"
        client_socket.send(message.encode())

        # Close the client socket
        client_socket.close()

if __name__ == "__main__":
    start_server()


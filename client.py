# tcp_client.py

import socket

HOST = '127.0.0.1'
PORT = 5030

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    http_request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client_socket.sendall(http_request.encode())

    response = b""
    while True:
        part = client_socket.recv(1024)
        if not part:
            break
        response += part

print("[CLIENT] Received response:")
print(response.decode())


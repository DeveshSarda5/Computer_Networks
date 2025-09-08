# tcp_server.py

import socket

HOST = '0.0.0.0'
PORT = 5056

html_content = """
<html>
<head><title>My Simple TCP Web Server</title></head>
<body>
  <h1>Welcome to My TCP Web Server!</h1>
  <p>This is a basic HTML page served over TCP.</p>
</body>
</html>
"""

response = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: {len(html_content)}

{html_content}"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[SERVER] Listening on http://{HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            request = conn.recv(1024).decode()
            print(f"[SERVER] Request:\n{request}")

            conn.sendall(response.encode())
            print("[SERVER] Response sent")


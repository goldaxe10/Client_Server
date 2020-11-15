import socket


while True:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('DESKTOP-24EDK13', 5000))
    x = input().encode('utf-8')
    server_socket.send(x)
    server_socket.close()
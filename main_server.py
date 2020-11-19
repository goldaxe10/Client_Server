import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('DESKTOP-24EDK13', 5000))
server_socket.listen(5)

while True:
    print('before .accept()')
    client_socket, addr = server_socket.accept()
    print('connection from', addr)
    client_socket.sendall('start_scan'.encode())
    print('sended message  \'start scan\' to', addr)
    result = client_socket.recv(4096)
    print(result.decode('utf-8'))
print('stop')
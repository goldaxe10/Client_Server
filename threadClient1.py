import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('MASTER-PC01', 5000))

server_socket.send(b'test')
server_message = server_socket.recv(64)
print('R', server_message)
server_socket.close()
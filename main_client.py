import socket


#while True:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('MASTER-PC01', 5000))
while True:
    x = input().encode('utf-8')
    if x.decode('utf-8') == 'quit()':
        server_socket.send(x)
        server_socket.close()
        break
    else:
        server_socket.send(x)

    #server_socket.close()
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('DESKTOP-24EDK13', 5000))
server_socket.listen(5)

while True:
    try:
        print('before .accept()')
        client_socket, addr = server_socket.accept()
        print('connection from', addr)
    except KeyboardInterrupt:
        server_socket.close()
        break
    else:
        result = client_socket.recv(4096)
        client_socket.close()
        print(result.decode('utf-8'))
        
        #if result.decode('utf-8') == 'Test':
        #    print('alarm')
        #else:
        #    print('sdfsd')
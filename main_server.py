import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('MASTER-PC01', 5000))
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
        while True:
            result = client_socket.recv(4096)
            if result.decode('utf-8') == 'quit()':
                client_socket.close()
                break
            else:
        #client_socket.close()
                print(result.decode('utf-8'))
        
        #if result.decode('utf-8') == 'Test':
        #    print('alarm')
        #else:
        #    print('sdfsd')
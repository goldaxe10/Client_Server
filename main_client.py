import socket
import os
import time

def start_script(path_to_folder='C:\\1'):
    while True:
        if len(os.listdir(path_to_folder)) != 0:
            time.sleep(2)
            cnt_of_files = len(os.listdir(path_to_folder))
            client_message = 'Error! ' + 'найдено файлов: ' + str(cnt_of_files)
            break
    return client_message

hostname = 'DESKTOP-24EDK13'
port = 5000
sock_recv = 4096
#hostname = socket.gethostname()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((hostname, port))
server_message = server_socket.recv(sock_recv)

if server_message.decode('utf-8') == 'start_scan':
    print('start_scan')

    message_start_script = start_script()
    print(message_start_script)
    server_socket.send(message_start_script.encode())
else:
    server_socket.send('unknown_request'.encode())
    print('unknown_request')

server_socket.close()

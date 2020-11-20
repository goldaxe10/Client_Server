import socket
import os
import time

def start_script(path_to_folder='C:\\1'):
    while True:
        if len(os.listdir(path_to_folder)) != 0:
            time.sleep(2)
            cnt_of_files = len(os.listdir(path_to_folder))
            client_message = 'Warning! ' + 'найдено файлов: ' + str(cnt_of_files)
            break
    return client_message

hostname = 'MASTER-PC01'
port = 5000
sock_recv = 4096
stand_host_name = socket.gethostname()
path_to_folder = 'C:\\1'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((hostname, port))
server_message = server_socket.recv(sock_recv)

if server_message == b'start_scan':
    print('start_scan')
    message_start_script = start_script()
    print(message_start_script)
    server_socket.send(message_start_script.encode() + ' from stand: {}'.format(stand_host_name).encode())
else:
    #uknow_request = b'uknow_request'
    server_socket.send(b'uknow_request')
    print('uknow_request')

server_socket.close()
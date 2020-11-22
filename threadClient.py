import socket
import os
import time


def connect_to_command_server(hostname, port, sock_recv):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((hostname, port))
    server_message = server_socket.recv(sock_recv)
    server_socket.send(b'connection OK')
    server_socket.close()
    return server_message


def connect_to_message_server(hostname, port, message_to_message_server=b'Empty message'):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((hostname, port))
    server_socket.send(message_to_message_server)
    server_socket.close()


def start_scan(path_to_folder=r'C:\1'):
    while True:
        if len(os.listdir(path_to_folder)) != 0:
            time.sleep(2)
            cnt_of_files = len(os.listdir(path_to_folder))
            client_message = 'Warning! ' + 'найдено файлов: ' + str(cnt_of_files)
            break
    return client_message


def start_script():
    connection_message = connect_to_command_server('DESKTOP-24EDK13', 5000, 4096)
    stand_host_name = socket.gethostname()
    path_to_folder = r'C:\1'

    try:
        if connection_message == b'start_scan':
            print('start_scan')
            message_start_script = start_scan(path_to_folder)
            print(message_start_script)
            message_to_message_server = message_start_script.encode() + ' from stand {}'.format(stand_host_name).encode()
            connect_to_message_server('DESKTOP-24EDK13', 5001, message_to_message_server)
        else:
            message = b'unknown_request'
            connect_to_message_server('DESKTOP-24EDK13', 5001, message)
            print('unknown_request: "{}"'.format(connection_message.decode('utf-8')))

    except ConnectionRefusedError:
        print("can't connect to message server")


if __name__ == '__main__':
    start_script()

import socket
import os
import datetime
import time

def start_script():
    while True:
        if len(os.listdir(path_to_folder)) == 0:
            print('Объекты не найдены')
        else:
            for files in (os.listdir(path_to_folder)):
                os.chdir(path_to_folder)
                print('Объект найден -->', files, datetime.datetime.fromtimestamp(os.path.getctime(files)).strftime('[%d %B, %Y, %H:%M:%S]')) 
            break
        time.sleep(5)

path_to_folder = ('C:\\1')
#start_script()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect(('DESKTOP-24EDK13', 5000))
x = input().encode('utf-8')
server_socket.send(x)
server_socket.close()
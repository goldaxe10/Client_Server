import socketserver
import os
import subprocess


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):
    #psexec = r'D:\Github\Client_Server\PsExec64.exe'
    #subprocess.call([psexec, r'\\DESKTOP-24EDK13', '-i', '-s', '-h', '-d', r'D:\Github\Client_Server\threadClient.py'])
    os.startfile(r'D:\Github\Client_Server\threadClient.py')

    def handle(self):
        #os.startfile(r'D:\Github\Client_Server\threadClient.py')

        command = input("Please enter the command 'start_scan' for scanning files in target directory: ").encode()
        #command = b'start_scan'
        print(' Send to client: {}'.format(command.decode()))
        self.request.sendall(command)
        client_response = self.request.recv(1024)  # .strip()
        print(' Response from client: {}'.format(self.client_address[0]), '\n',
              'Message: {}'.format(client_response.decode('utf-8')))


if __name__ == "__main__":
    with ThreadingTCPServer(('DESKTOP-24EDK13', 5000), EchoTCPHandler) as server_socket:
        server_socket.serve_forever()

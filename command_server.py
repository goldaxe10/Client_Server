import socketserver
import os
import subprocess


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):
    print("Please enter the command: start_scan for scanning files in target directory: ", end='')
    #psexec = r'D:\Github\Client_Server\PsExec64.exe'
    #subprocess.call(
        #[psexec,'DESKTOP-24EDK13' , '-i', '-s', '-h', '-d', 'defrag', 'C:', '/D'])

    def handle(self):
        command = input().encode()
        #data = b'start_scan'
        print(' Send to client: {}'.format(command.decode()))
        self.request.sendall(command)
        client_response = self.request.recv(1024)  # .strip()
        print(' Response from client: {}'.format(self.client_address[0]), '\n',
              'Message: {}'.format(client_response.decode('utf-8')))


if __name__ == "__main__":
    with ThreadingTCPServer(('DESKTOP-24EDK13', 5000), EchoTCPHandler) as server_socket:
        server_socket.serve_forever()

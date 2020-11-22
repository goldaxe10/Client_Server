import socketserver
import os


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):
    for i in range(100):
        os.startfile(r'D:\Github\Client_Server\threadClient.py')

    def handle(self):
        #os.startfile(r'D:\Github\Client_Server\threadClient.py')
        command = b'start_scan'
        #command = input("Please enter the command 'start_scan' for scanning files in target directory: ").encode()
        print(' Send to client: {}'.format(command.decode()))
        self.request.sendall(command)
        client_response = self.request.recv(1024)  # .strip()
        print(' Response from client: {}'.format(self.client_address[0]), '\n',
              'Message: {}'.format(client_response.decode('utf-8')))


if __name__ == "__main__":
    with ThreadingTCPServer(('DESKTOP-24EDK13', 5000), EchoTCPHandler) as server_socket:
        server_socket.serve_forever()
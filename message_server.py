import socketserver
import os
import subprocess


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        #data = b'start_scan'
        #print(' Send to client: {}'.format(data.decode()))
        #self.request.sendall(data)
        client_response = self.request.recv(1024)  # .strip()
        print(' Response from client: {}'.format(self.client_address[0]), '\n',
              'Message: {}'.format(client_response.decode('utf-8')))


if __name__ == "__main__":
    with ThreadingTCPServer(('DESKTOP-24EDK13', 5001), EchoTCPHandler) as server_socket:
        server_socket.serve_forever()

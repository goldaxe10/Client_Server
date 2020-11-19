import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_input = input()
        data = data_input.encode('utf-8')
        #print('Addres: {}'.format(self.client_address[0]))
        print(' Send to client: {}'.format(data.decode()))
        self.request.sendall(data)
        client_response = self.request.recv(1024)#.strip()
        print(' Response from client: {}'.format(self.client_address[0]),'\n', 'Message: {}'.format(client_response.decode('utf-8')))

if __name__ == "__main__":
    with ThreadingTCPServer(('DESKTOP-24EDK13', 5000), EchoTCPHandler) as server_socket:
        server_socket.serve_forever()

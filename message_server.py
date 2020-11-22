import socketserver
import os
import subprocess
import datetime


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):
    datetoday = datetime.datetime.today().strftime(
        "%d-%m-%Y_%Hh%Mm%Ss")  # + "_" + datetime.datetime.today().strftime("%H:%M:%S")

    def handle(self):
        datetoday = datetime.datetime.today().strftime(
            "%d-%m-%Y_%Hh%Mm%Ss")  # + "_" + datetime.datetime.today().strftime("%H:%M:%S")

        client_response = self.request.recv(1024)  # .strip()
        message_from_client = ' Response from client: {}'.format(self.client_address[0]) + '\n' + 'Message: {}'.format(
            client_response.decode('utf-8')) + '\n'
        print(message_from_client)
        with open('D:\Github\Client_Server\logs\log.log', 'a') as logs:
            logs.write(datetoday + message_from_client + '\n')


if __name__ == "__main__":
    with ThreadingTCPServer(('DESKTOP-24EDK13', 5001), EchoTCPHandler) as server_socket:
        server_socket.serve_forever()

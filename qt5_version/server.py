from socket import *
import json

PORT = 6666

class Server:
    def __init__(self):
        self.serverPort = PORT
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('', self.serverPort))
        self.serverSocket.listen(2)
        print('Ready to connect...')

        self.player1, self.addr1 = self.serverSocket.accept()
        data1 = {'type': 'color', 'data': 1}
        print('Player1 connected')

        self.player2, self.addr2 = self.serverSocket.accept()
        data2 = {'type': 'color', 'data': 0}
        print('Player2 connected')

        self.player1.sendall(self.packSocket(data1))
        print("Send to player1", data1)
        self.player2.sendall(self.packSocket(data1))
        print("Send to player2", data2)

        print('Read to receive...')


    def run(self):
        sentence = self.player1.recv(1024).decode()
        if sentence == '':
            self.close()
        print('received from ', self.addr1, ': ', sentence)
        self.player2.send(sentence.encode())
        self.player1, self.player2 = self.player2, self.player1
        self.addr1, self.addr2 = self.addr2, self.addr1

    def close(self):
        self.player1.close()
        self.player2.close()

    def packSocket(self, data):
        return (json.dumps(data) + ' END').encode()
        

if __name__ == '__main__':
    server = Server()
    while True:
        server.run()



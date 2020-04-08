from socket import *

PORT = 6666

class Server:
    def __init__(self):
        self.serverPort = PORT
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('', self.serverPort))
        self.serverSocket.listen(2)
        print('Ready to connect...')
        self.player1, self.addr1 = self.serverSocket.accept()
        self.player1.send('#1'.encode())
        print('Player1 connected')
        self.player2, self.addr2 = self.serverSocket.accept()
        self.player2.send('#0'.encode())
        print('Player2 connected')
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
        
if __name__ == '__main__':
    server = Server()
    while True:
        server.run()



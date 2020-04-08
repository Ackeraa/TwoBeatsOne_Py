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
        print('Player1 connected')

    def run(self):
        sentence = self.player1.recv(1024).decode()
        if sentence == '':
            self.close()
        print('received from ', self.addr1, ': ', sentence)
        self.player1.send(sentence.encode())

    def close(self):
        self.player1.close()
        
if __name__ == '__main__':
    server = Server()
    while True:
        server.run()



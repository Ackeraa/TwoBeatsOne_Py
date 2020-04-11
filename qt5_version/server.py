from socket import *
import json
import threading

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

        self.player2, self.addr2 = self.serverSocket.accept()
        print('Player2 connected')

        data1 = {'type': 'color', 'data': 1}
        self.player1.sendall(self.packSocket(data1))
        print("Send to player1", data1)

        data2 = {'type': 'color', 'data': 0}
        self.player2.sendall(self.packSocket(data2))
        print("Send to player2", data2)

        print('Start to create threading...')
        threading.Thread(target=self.run, args=(self.player1, self.player2,)).start() #first player
        threading.Thread(target=self.run, args=(self.player2, self.player1,)).start() #second player
        print('Threading created, start to communicate')


    def run(self, own, opp):
        while True:
            sentence = own.recv(1024).decode()
            if sentence == '':
                self.close()
            print('received: ', sentence)
            opp.send(sentence.encode())

    def close(self):
        self.player1.close()
        self.player2.close()

    def packSocket(self, data):
        return (json.dumps(data) + ' END').encode()


if __name__ == '__main__':
    server = Server()



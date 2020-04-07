import pygame as pg
from os import path
from settings import *
from socket import *

class Network:
    def __init__(self, game):
        self.serverName = SERVERNAME
        self.serverPort = PORT
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((self.serverName, self.serverPort))
        color = self.clientSocket.recv(1024).decode()
        game.color = int(color[1])

        #need to check if connected
        print('Connect Successfully with color: ', game.color)

    def send(self, source, dest):
        #source: the selected piece
        #dest: the position to move
        sentence = str(source[0]) + ' ' + str(source[1]) + ' ' + str(dest[0]) + ' ' + str(dest[1]) 
        self.clientSocket.send(sentence.encode())
    
    def receive(self):
        sentence = self.clientSocket.recv(1024).decode()
        return sentence

    def close(self):
        self.clientSocket.close()


    




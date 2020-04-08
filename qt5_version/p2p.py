import socket
import pygame
import random
import json
import threading
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from settings import *

class P2p(QWidget):

    backSignal = pyqtSignal()
    exitSignal = pyqtSignal()
    recvSignal = pyqtSignal(dict, name = 'data')
    send_back_signal = False

    def __init__(self, own, opp, ownName, serverName):
        super().__init__()

        self.ownName = ownName
        self.oppName = None
        self.serverPort  = PORT
        self.isRunning = False
        
        self.selected = [-1, -1] #piece that selected
        self.moveTo = [-1, -1] #where to move 
        self.board = [[-1 for _ in range(LINES)] for _ in range(LINES)]
        for i in range(LINES):
            self.board[i][LINES - 1] = own 
            self.board[i][0] = opp 

        self.recvSignal.connect(self.transData)

        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpSocket.connect((SERVERNAME, PORT))
        data = {'type': 'ownName', 'data': self.ownName}
        self.tcpSocket.sendall(self.packSocket(data))
        
        threading.Thread(target = self.recvData).start()
        #start a threading listening server


        self.setFixedSize(750, 750)
        self.setWindowTitle('Two Beats One')
        #self.setWindowIcon(QIcon(ICON_FILEPATH))
        
        #bgi
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap(BACKGROUND_IMAGEPATHS.get('bg_game'))))
        self.setPalette(palette)

    #to transcation data received
    def transData(self, data):
        print("FUCK")
        print(data)

    def recvData(self):
        while True:
            data = self.unPackSocket()
            print(data)
            self.recvSignal.emit(data)

    def packSocket(self, data):
        return (json.dumps(data) + ' END').encode()

    def unPackSocket(self):
        data = ''
        while True:
            dataPart = self.tcpSocket.recv(1024).decode()
            if 'END ' in dataPart:
                data += dataPart[:dataPart.index('END')]
                break
            data += dataPart
        return json.loads(data, encoding = 'utf-8')
        


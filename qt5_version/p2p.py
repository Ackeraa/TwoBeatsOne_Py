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
       # self.tcpSocket.connect((SERVERNAME, PORT))
        data = {'type': 'ownName', 'data': self.ownName}
       # self.tcpSocket.sendall(self.packSocket(data))
        
        #start a threading listening server
        threading.Thread(target = self.recvData).start()


        #set bgi
        bgi = QPixmap('bg7.jpg')
        bgi = bgi.scaled(900, 750)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(bgi))
        self.setPalette(palette)

        #set layout
        self.creatBoardWindow()
        self.creatChatWindow()
        layout = QHBoxLayout()
        layout.addLayout(self.boardWindow)
        layout.addLayout(self.chatWindow)
        self.setLayout(layout)

        self.resize(900, 750)
        self.show()

    def creatBoardWindow(self):
        self.boardWindow = QVBoxLayout()
        
        #creat button
        buttonLayout = QHBoxLayout()
        
        self.startBtn = QPushButton('开始', self)
        self.backBtn = QPushButton('悔棋', self)
        self.giveUpBtn = QPushButton('认输', self)
        self.exitBtn = QPushButton('退出', self)

        buttonLayout.setSpacing(10) 
        buttonLayout.addWidget(self.startBtn)
        buttonLayout.addWidget(self.backBtn)
        buttonLayout.addWidget(self.giveUpBtn)
        buttonLayout.addWidget(self.exitBtn)

        #creat chess board

        bgi = QPixmap('board1.png')
        bgi = bgi.scaled(600, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
        board = QLabel()
        board.setPixmap(bgi)

        self.boardWindow.addLayout(buttonLayout)
        self.boardWindow.addWidget(board)

    def creatChatWindow(self):
        self.chatWindow = QVBoxLayout()

        nameLabel = QLabel("Chat Window")
        self.recvField = QTextEdit()
        self.sendField = QTextEdit()
        self.sendBtn = QPushButton('发送')

        self.recvField.setFocusPolicy(Qt.NoFocus) 

        self.chatWindow.setSpacing(2)
        self.chatWindow.addWidget(nameLabel)
        self.chatWindow.addWidget(self.recvField)
        self.chatWindow.addWidget(self.sendField)
        self.chatWindow.addWidget(self.sendBtn)

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
        


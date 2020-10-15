import socket
import pygame
import random
import json
import threading
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from settings import *
from board import *
from tools import *
from chat import *
from buttons import *

class P2p(QWidget):

    backSignal = pyqtSignal()
    exitSignal = pyqtSignal()
    recvSignal = pyqtSignal(dict, name = 'data')
    send_back_signal = False

    def __init__(self, own, opp, ownName, serverName):
        super().__init__()

        self.ownName = 'own'
        self.oppName = 'opp'
        self.serverPort  = PORT
        self.board = Board()

        self.recvSignal.connect(self.transData)


        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcpSocket.connect((SERVERNAME, PORT))
        data = {'type': 'ownName', 'data': self.ownName}
        self.tcpSocket.sendall(packSocket(data))
        
        #start a threading listening server
        threading.Thread(target = self.recvData).start()

        #set bgi
        bgi = QPixmap(BACKGROUND_IMAGEPATHS.get('game_bgi'))
        bgi = bgi.scaled(900, 750)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(bgi))
        self.setPalette(palette)

        #set layout
        self.creatBoardWindow()
        self.creatChatWindow()
        layout = QHBoxLayout()
        layout.setSpacing(20)
        layout.addLayout(self.boardWindow)
        layout.addLayout(self.chatWindow)
        self.setLayout(layout)

        self.setFixedSize(900, 750)
        self.center()


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            x = e.x()
            y = e.y()
            data = self.board.ownMove([x, y])
            if data != -1:
                if data['type'] == 'result' and data['data'] == 'win':
                    pass
                self.tcpSocket.sendall(packSocket(data))

            text = "x: {0}, y: {1}".format(x, y)
           # self.sendField.setText(text)
            self.sendField.clear()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def creatBoardWindow(self):
        self.boardWindow = QVBoxLayout()
        self.boardWindow.setSpacing(2)
        
        #creat button
        buttonLayout = QHBoxLayout()
        
        self.startBtn = Button('开始', self)
        self.backBtn = Button('悔棋', self)
        self.giveUpBtn = Button('认输', self)
        self.exitBtn = Button('退出', self)

        buttonLayout.setSpacing(10) 
        buttonLayout.addWidget(self.startBtn)
        buttonLayout.addWidget(self.backBtn)
        buttonLayout.addWidget(self.giveUpBtn)
        buttonLayout.addWidget(self.exitBtn)

        #creat chess board
        bgi = QPixmap(BACKGROUND_IMAGEPATHS.get('board_bgi'))
        bgi = bgi.scaled(600, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
        board = QLabel(self)
        board.setPixmap(bgi)

        self.boardWindow.addLayout(buttonLayout)
        self.boardWindow.addWidget(board)

    def creatChatWindow(self):
        self.chatWindow = QVBoxLayout()

        nameLabel = TitleField()
        self.recvField = ReceiveField()
        self.sendField = SendField(self)

        self.chatWindow.setSpacing(0)
        self.chatWindow.addWidget(nameLabel)
        self.chatWindow.addWidget(self.recvField)
        self.chatWindow.addWidget(self.sendField)

    #Be ready

    #chat
    def sendMessage(self, message):
        data = {'type': 'chat', 'data': message}
        #show in own screen
        self.recvField.showMessage(self.ownName, 'own', data['data'])
        #send
        self.tcpSocket.sendall(packSocket(data)) 

    #to transcation data received
    def transData(self, data):
        print('transData:', data)
        if data['type'] == 'move':
            source = data['source']
            dest = data['dest']
            print(source, dest)
            isLost = self.board.oppMove(source, dest)
            if isLost:
                pass
        elif data['type'] == 'color':
            self.board.setPiece(self, int(data['data']))
        elif data['type'] == 'chat':
            self.recvField.showMessage(self.oppName, 'opp', data['data'])


    def recvData(self):
        while True:
            data = unPackSocket(self.tcpSocket)
            print(data)
            self.recvSignal.emit(data)


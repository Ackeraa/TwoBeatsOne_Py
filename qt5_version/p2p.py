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
        self.board = Board()

        self.recvSignal.connect(self.transData)

        self.tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       # self.tcpSocket.connect((SERVERNAME, PORT))
        data = {'type': 'ownName', 'data': self.ownName}
       # self.tcpSocket.sendall(packSocket(data))
        
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

        self.resize(900, 750)
        self.center()

        self.board.setPiece(self, 0)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:

            x = e.x()
            y = e.y()
            self.board.ownMove([x, y])

            text = "x: {0}, y: {1}".format(x, y)
            self.sendField.setText(text)


    def center(self):

        print("FUUUUUUUUUUUU")
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def creatBoardWindow(self):
        self.boardWindow = QVBoxLayout()
        self.boardWindow.setSpacing(20)
        
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
        bgi = QPixmap(BACKGROUND_IMAGEPATHS.get('board_bgi'))
        bgi = bgi.scaled(600, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
        board = QLabel(self)
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
            data = unPackSocket(self.tcpSocket)
            print(data)
            self.recvSignal.emit(data)


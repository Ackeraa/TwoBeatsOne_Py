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
from aiSearch import *
from gameState import *

class P2c(QWidget):

    def __init__(self, own, opp):
        super().__init__()

        #set bgi
        bgi = QPixmap(BACKGROUND_IMAGEPATHS.get('game_bgi'))
        bgi = bgi.scaled(650, 700)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(bgi))
        self.setPalette(palette)

        #set layout
        self.creatBoardWindow()
        layout = QHBoxLayout()
        layout.setSpacing(200)
        layout.addLayout(self.boardWindow)
        self.setLayout(layout)

        self.board = Board(48, 100)
        self.board.setPiece(self, own)

        self.setFixedSize(650, 700)
        self.center()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            x = e.x()
            y = e.y()
            print(x, y)
            self.board.ownMove([x, y])
            state = gameState(self.board.own_pieces, self.board.opp_pieces)
            aiSearch = AISearch(state)
            result = aiSearch.search()
            self.board.oppMove(result[0], result[1])

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


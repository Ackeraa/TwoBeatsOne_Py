import socket
import pygame
import random
import json
import threading
import multiprocessing
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

class P2c(QWidget):

    def __init__(self, own, opp):
        super().__init__()

        self.own = own
        self.moved = 0
        self.lose = 0
        #listen if moved
        threading.Thread(target = self.ai_move).start()

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

    def new(self):

        for i in range(len(self.board.ownPieces)):
            piece = self.board.ownPieces[i]
            if piece != None:
                piece.deleteLater()
                self.board.ownPieces[i] = None

        for i in range(len(self.board.oppPieces)):
            piece = self.board.oppPieces[i]
            if piece != None:
                piece.deleteLater()
                self.board.oppPieces[i] = None

        self.moved = 0
        self.board = Board(48, 100)
        self.board.setPiece(self, self.own)

        self.setFixedSize(650, 700)
        self.center()

    def ai_move(self):
        while True:
            if self.moved == 1:
                self.moved = 0
                aiSearch = AISearch(1 - self.own, self.board.oppPieces, self.board.ownPieces, SIMULATIONS, SEARCH_DEPTH)
                result = aiSearch.search()
                print("FUUUULK", result)
                is_lose = self.board.oppMove(result[0], result[1])
                if is_lose:
                    print("LOSE")
                    self.lose = 1

    def mousePressEvent(self, e):
        if self.lose:
            self.lose = 0
            self.new()

        if e.button() == Qt.LeftButton:
            x = e.x()
            y = e.y()
            print(x, y)
            result = self.board.ownMove([x, y])
            if result["type"] == "result" and  result["data"] == "win":
                print("WIN")
                self.new() 
            if result["type"] == "move":
                self.moved = 1
                print("TESZT ", self.moved)

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


import socket
import pygame
import random
import json
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
import threading
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

        #listen if moved
        self.own_moved = 0
        self.opp_moved = 1
        threading.Thread(target = self.move_own).start()
        threading.Thread(target = self.move_opp).start()

        self.setFixedSize(650, 700)
        self.center()

    def new(self):

        self.own_moved = 0
        self.opp_moved = 1
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

        self.board = Board(48, 100)
        self.board.setPiece(self, self.own)

        self.setFixedSize(650, 700)
        self.center()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            p1 = AISearch(self.own, self.board.ownPieces, self.board.oppPieces, SIMULATIONS, SEARCH_DEPTH, 0)
            result = p1.search()
            print("-----OWN-----", result)
            is_lose = self.board.ownMove1(result[0], result[1])
            QApplication.processEvents()
            time.sleep(1)
            if is_lose:
                print("lose")
                self.new()
            p2 = AISearch(1 - self.own, self.board.oppPieces, self.board.ownPieces, SIMULATIONS, SEARCH_DEPTH, 1)
            result = p2.search()
            print("-----OPP-----", result)
            is_lose = self.board.oppMove(result[0], result[1])
            QApplication.processEvents()
            if is_lose:
                print("lose")
                self.new()

    def move_own(self):
        while True:
            if self.opp_moved:
                p1 = AISearch(self.own, self.board.ownPieces, self.board.oppPieces, SIMULATIONS, SEARCH_DEPTH, 0)
                result = p1.search()
                print("-----OWN-----", result)
                is_lose = self.board.ownMove1(result[0], result[1])
                if is_lose:
                    print("lose")
                    self.new()
                self.opp_moved = 0
                self.own_moved = 1

    def move_opp(self):
        while True:
            if self.own_moved:
                p2 = AISearch(1 - self.own, self.board.oppPieces, self.board.ownPieces, SIMULATIONS, SEARCH_DEPTH, 1)
                result = p2.search()
                print("-----OPP-----", result)
                is_lose = self.board.oppMove(result[0], result[1])
                QApplication.processEvents()
                if is_lose:
                    print("lose")
                self.own_moved = 0
                self.opp_moved = 1

    '''
    def mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            x = e.x()
            y = e.y()
            print(x, y)
            result = self.board.ownMove([x, y])
            if result["type"] == "result" and  result["data"] == "win":
                print("WIN")
                self.new() 
            if result["type"] == "move":
                QApplication.processEvents()
                aisearch = aisearch(1 - self.own, self.board.opppieces, self.board.ownpieces, simulations, search_depth)
                result = aisearch.search()
                print("fuuuulk", result)
                is_lose = self.board.oppmove(result[0], result[1])
                if is_lose:
                    print("lose")
                    self.new()
    '''

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

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=P2c(1, 0)
    win.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from settings import *
from tools import *

class Piece(QLabel):
    def __init__(self, grandParent, parent, color, pos):
        super(Piece, self).__init__(grandParent)

        self.color = color 
        self.parent = parent
        image = None 
        if color == 0:
            image = QPixmap(PIECEPATH.get('white'))
        else:
            image = QPixmap(PIECEPATH.get('black'))
        self.setFixedSize(image.size())
        self.setPixmap(image)
        self.move(pos)
        self.show()
    
    def move(self, pos):
        self.pos = pos
        pos = i2p(pos) 
        super().move(pos[0] - PIECE_SIZE, pos[1] - PIECE_SIZE)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            if self.color == self.parent.own:
                self.parent.selected = self
                print("Selected: ", self.pos)


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from settings import *
from tools import *

class Piece(QLabel):
    def __init__(self, grandParent, parent, color, pos, X0, Y0):
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
        self.move(pos, X0, Y0)
        self.show()
    
    def move(self, pos, X0, Y0):
        self.pos = pos
        pos = i2p(pos, X0, Y0) 
        super().move(pos[0] - PIECE_SIZE, pos[1] - PIECE_SIZE)
        QApplication.processEvents()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            if self.color == self.parent.own:
                self.parent.selected = self
                print("Selected: ", self.pos)


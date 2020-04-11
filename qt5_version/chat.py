import json
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from settings import *
from tools import *

class SendField(QTextEdit):
    def __init__(self, parent):
        QTextEdit.__init__(self)

        self.parent = parent

    def keyPressEvent(self, e):
        QTextEdit.keyPressEvent(self,e)
        if e.key() == Qt.Key_Return:
            self.parent.sendMessage(self.toPlainText()[:-1])
            self.clear()

class ReceiveField(QTextEdit):
    def __init__(self):
        QTextEdit.__init__(self)

        self.setFocusPolicy(Qt.NoFocus) 
    
        #self.setFontFamily('consolas')

    def showMessage(self, name, who, message):
        if who == 'own':
            self.setTextColor(Qt.red)
        else:
            self.setTextColor(Qt.blue)
        self.setFontPointSize(16)
        self.setFontWeight(20)
        self.append(name + ':')
        self.setFontPointSize(10)
        self.append("")
        self.setFontPointSize(18)
        self.append(message)
        print('Message showed', message)
        self.append("")


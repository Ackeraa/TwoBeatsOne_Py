import json
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from settings import *
from tools import *

class TitleField(QLabel):
    def __init__(self):
        QLabel.__init__(self)
        
        self.setFixedSize(250, 40);
        self.setText("                聊天窗口")
        self.setStyleSheet("background-image:url(title.png);font-size: 20px; color:#28085D; font-family:STKaiti")


class SendField(QTextEdit):
    def __init__(self, parent):
        QTextEdit.__init__(self)


        self.parent = parent
        self.setStyleSheet("background-image:url(send.jpeg)")
        self.setFixedSize(250, 100);

    def keyPressEvent(self, e):
        QTextEdit.keyPressEvent(self,e)
        if e.key() == Qt.Key_Return:
            self.parent.sendMessage(self.toPlainText()[:-1])
            self.clear()

class ReceiveField(QTextEdit):
    def __init__(self):
        QTextEdit.__init__(self)

        self.setFocusPolicy(Qt.NoFocus) 
        self.setStyleSheet("background-image:url(recv.jpeg)")
        self.setFixedSize(250, 400);
    
        #self.setFontFamily('consolas')

    def showMessage(self, name, who, message):
        self.setFontPointSize(13)
        self.setFontWeight(20)
        self.setTextColor(Qt.black)
        self.append(name + ':')
        if who == 'own':
            self.setTextColor(Qt.red)
        else:
            self.setTextColor(Qt.blue)
        self.setFontPointSize(5)
        self.append("")
        self.setFontPointSize(14)
        self.append("    " + message)
        print('Message showed', message)
        self.append("")


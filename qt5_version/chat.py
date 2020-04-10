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


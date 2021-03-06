from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class PushButton(QLabel):
    click_signal = pyqtSignal()
    need_emit = False
    def __init__(self, imagepaths, parent = None, **kwargs):
        super(PushButton, self).__init__(parent)

        self.image_0 = QPixmap(imagepaths[0])
        self.image_1 = QPixmap(imagepaths[1]) 
        self.image_2 = QPixmap(imagepaths[2]) 
        self.resize(self.image_0.size())
        self.setPixmap(self.image_0)
        self.setMask(self.image_1.mask())

    def enterEvent(self, event):
        self.setPixmap(self.image_1)

    def leaveEvent(self, event):
        self.setPixmap(self.image_0)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.need_emit = True
            self.setPixmap(self.image_2)

    def mouseReleaseEvent(self, event):
        if self.need_emit:
            self.need_emit = False
            self.setPixmap(self.image_1)
            self.click_signal.emit()

class Button(QLabel):
    click_signal = pyqtSignal()
    need_emit = False

    def __init__(self, name, parent = None):
        super(Button, self).__init__(parent)

        self.setFixedSize(100, 40);
        self.setText("     " + name)
        self.setStyleSheet("background-image:url(button.png);font-size: 20px; color:#28085D;font-family:STKaiti")

    def mousePressEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            self.need_emit = True

    def mouseReleaseEvent(self, e):
        if self.need_emit:
            self.need_emit = False
            self.click_signal.emit()

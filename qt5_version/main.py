import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from settings import *
from buttons import *
from p2p import *
from p2c import P2c

class gameStartUI(QWidget):
    def __init__(self, parent = None, **kwargs):
        super(gameStartUI, self).__init__(parent)

        self.playWithAI()
        '''
        self.setFixedSize(760, 650)
        self.setWindowTitle('Two Beats One')
        #self.setWindowIcon(QIcon(cfg.ICON_FILEPATH))
        
        #bgi
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap(BACKGROUND_IMAGEPATHS.get('start_bgi'))))
        self.setPalette(palette)

        #button
        #p2c
        self.ai_button = PushButton(BUTTON_IMAGEPATHS.get('ai'), self)
        self.ai_button.move(250, 200)
        self.ai_button.show()
        self.ai_button.click_signal.connect(self.playWithAI)
        #p2p
        self.online_button = PushButton(BUTTON_IMAGEPATHS.get('online'), self)
        self.online_button.move(250, 350)
        self.online_button.show()
        self.online_button.click_signal.connect(self.playOnline)
        '''

    def playOnline(self):
        self.close()
        self.game_type = P2p(0, 1, 'a', 6666)
        self.game_type.show()

    def playWithAI(self):
        self.close()
        self.game_type = P2c(1, 0)
        self.game_type.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    handle = gameStartUI()
    font = QFont()
    font.setPointSize(12)
    handle.setFont(font)
   # handle.show()
    sys.exit(app.exec_())


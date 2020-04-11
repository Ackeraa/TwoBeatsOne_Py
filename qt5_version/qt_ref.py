import sys
from PyQt5.QtWidgets import * 

from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        self.statusBar().showMessage('Ready')

        #menu
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu('&File')

        newAct = QAction('New', self)
        fileMenu.addAction(newAct)

        exitAct = QAction(QIcon('racecar.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct)
        fileMenu.addMenu(impMenu)
        

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 100)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',\
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class BoxLayout(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Tooltips')

        self.resize(750, 750)

        self.show()

class GridLayout(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):

            if name == '':
                continue 
            button = QPushButton(name)
            print(*position)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.show()

class TextField(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        self.reviewEdit = QTextEdit()
        self.reviewEdit.setFontFamily('consolas')
        self.reviewEdit.setTextColor (Qt.red)
        self.reviewEdit.setFontPointSize(20)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        
        grid.addWidget(review, 3, 0)
        grid.addWidget(self.reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.show()
    def mousePressEvent(self, e):
        self.reviewEdit.setFontWeight(100)
        self.reviewEdit.append("fucj")

class Signals(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

class MouseMove(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(text)

class Communicate(QObject):
    closeApp = pyqtSignal()
class Sender(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        #self.c = Communicate()#
        #self.c.closeApp.connect(self.close)#

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        sender.move(5, 5)
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def mousePressEvent(self, event):
        pass

        #self.c.closeApp.emit()


class InputDialog(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


class ProgressBar(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.resize(750, 750)
        self.show()

    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        self.setGeometry(300, 400, 200, 25)
        #creat button
        layout = QHBoxLayout()
        
        self.btn1 = QPushButton('开始', self)
        self.btn2 = QPushButton('悔棋', self)
        self.btn3 = QPushButton('认输', self)
        self.btn4 = QPushButton('退出', self)
        self.btn1.move(20, 20)
        '''
        layout.setSpacing(10) 
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
       
        self.setLayout(layout)
        '''

class BoardWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        bgi = QPixmap('board1.png')
        bgi = bgi.scaled(600, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
        board = QLabel(self)
        board.setPixmap(bgi)
        board.move(50, 50)


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        nameLabel = QLabel("Chat Window")
        self.recvField = QTextEdit()
        self.recvField.setFocusPolicy(Qt.NoFocus) 
        self.sendField = QTextEdit()
        self.sendBtn = QPushButton('发送')

        layout = QVBoxLayout()
        layout.setSpacing(2)
        layout.addWidget(nameLabel)
        layout.addWidget(self.recvField)
        layout.addWidget(self.sendField)
        layout.addWidget(self.sendBtn)

        self.setLayout(layout)
        self.move(1, 1)

class chessBoard(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):

        #set bgi
        bgi = QPixmap('bg7.jpg')
        bgi = bgi.scaled(900, 750)
        palette = QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(bgi))
        self.setPalette(palette)

        #import window
        self.boardWindow = BoardWindow()
        self.menuWindow = MenuWindow()
        self.chatWindow = ChatWindow()
        btn = QPushButton("Log in", self)
        btn.clicked.connect(btn.deleteLater)   
        #set layout
        leftLayout = QVBoxLayout()
        #leftLayout.addWidget(self.boardWindow)
        #leftLayout.addWidget(self.menuWindow)

        #layout = QHBoxLayout()
        #layout.addLayout(leftLayout)
        #layout.addWidget(self.chatWindow)
        #self.setLayout(layout)

        self.resize(900, 750)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = TextField()
    sys.exit(app.exec_())

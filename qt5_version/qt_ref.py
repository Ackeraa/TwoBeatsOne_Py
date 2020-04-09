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
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.show()

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

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

    def mousePressEvent(self, event):

        self.c.closeApp.emit()


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
        
class Testtt(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.createGridGroupBox()
        self.creatVboxGroupBox()
        self.creatFormGroupBox()
        mainLayout = QVBoxLayout()
        hboxLayout = QHBoxLayout()
        hboxLayout.addStretch()  
        hboxLayout.addWidget(self.gridGroupBox)
        hboxLayout.addWidget(self.vboxGroupBox)
        mainLayout.addLayout(hboxLayout)
        mainLayout.addWidget(self.formGroupBox)
        self.setLayout(mainLayout)

        self.resize(750, 750)
        self.show()

    def createGridGroupBox(self):
        self.gridGroupBox = QGroupBox("Grid layout")
        layout = QGridLayout()

        nameLabel = QLabel("中文名称")
        nameLineEdit = QLineEdit("天宫二号")
        emitLabel = QLabel("发射地点")
        emitLineEdit = QLineEdit("酒泉中心")
        timeLabel = QLabel("发射时间")
        timeLineEdit = QLineEdit("9月15日")
        imgeLabel = QLabel()
        layout.setSpacing(10) 
        layout.addWidget(nameLabel,1,0)
        layout.addWidget(nameLineEdit,1,1)
        layout.addWidget(emitLabel,2,0)
        layout.addWidget(emitLineEdit,2,1)
        layout.addWidget(timeLabel,3,0)
        layout.addWidget(timeLineEdit,3,1)
        layout.addWidget(imgeLabel,0,2,4,1)
        layout.setColumnStretch(1, 10)
        self.gridGroupBox.setLayout(layout)
        self.setWindowTitle('Basic Layout')

    def creatVboxGroupBox(self):
        self.vboxGroupBox = QGroupBox("Vbox layout")
        layout = QVBoxLayout() 
        nameLabel = QLabel("科研任务：")
        bigEditor = QTextEdit()
        bigEditor.setPlainText("搭载了空间冷原子钟等14项应用载荷，以及失重心血管研究等航天医学实验设备 "
                "开展空间科学及技术试验.")
        layout.addWidget(nameLabel)
        layout.addWidget(bigEditor)
        self.vboxGroupBox.setLayout(layout)

    def creatFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        performanceLabel = QLabel("性能特点：")
        performanceEditor = QLineEdit("舱内设计更宜居方便天宫生活")
        planLabel = QLabel("发射规划：")
        planEditor = QTextEdit()
        planEditor.setPlainText("2020年之前，中国计划初步完成空间站建设")
        layout.addRow(performanceLabel,performanceEditor)
        layout.addRow(planLabel,planEditor)

        self.formGroupBox.setLayout(layout)

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

        #set layout
        self.creatBoardWindow()
        self.creatChatWindow()
        layout = QHBoxLayout()
        layout.addLayout(self.boardWindow)
        layout.addLayout(self.chatWindow)
        self.setLayout(layout)

        self.resize(900, 750)
        self.show()

    def creatBoardWindow(self):
        self.boardWindow = QVBoxLayout()
        
        #creat button
        buttonLayout = QHBoxLayout()
        
        self.btn1 = QPushButton('开始', self)
        self.btn2 = QPushButton('悔棋', self)
        self.btn3 = QPushButton('认输', self)
        self.btn4 = QPushButton('退出', self)

        buttonLayout.setSpacing(10) 
        buttonLayout.addWidget(self.btn1)
        buttonLayout.addWidget(self.btn2)
        buttonLayout.addWidget(self.btn3)
        buttonLayout.addWidget(self.btn4)

        #creat chess board

        bgi = QPixmap('board1.png')
        bgi = bgi.scaled(600, 600, Qt.KeepAspectRatio, Qt.FastTransformation)
        board = QLabel()
        board.setPixmap(bgi)

        self.boardWindow.addLayout(buttonLayout)
        self.boardWindow.addWidget(board)

    def creatChatWindow(self):
        self.chatWindow = QVBoxLayout()

        nameLabel = QLabel("Chat Window")
        self.recvField = QTextEdit()
        self.sendField = QTextEdit()
        self.sendBtn = QPushButton('发送')

        self.recvField.setFocusPolicy(Qt.NoFocus) 

        self.chatWindow.setSpacing(2)
        self.chatWindow.addWidget(nameLabel)
        self.chatWindow.addWidget(self.recvField)
        self.chatWindow.addWidget(self.sendField)
        self.chatWindow.addWidget(self.sendBtn)

class bgi(QWidget):

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

        self.setFixedSize(900, 750)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = chessBoard()
    sys.exit(app.exec_())

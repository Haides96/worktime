#from PyQt5 import QtCore
#from PyQt5 import QtGui
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #----Toolbar-----
        #
        #----------------
        exit2Action = QAction(QIcon('./images/web.png'), 'Exit', self)
        exit2Action.setShortcut('Ctrl+W')
        exit2Action.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit2Action)
        #--------Меню программы
        #Менюшка с кнопкой выхода из приложения
        #--------
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu2 = menubar.addMenu('&Users')
        #Exit
        exitAction = QAction(QIcon('./images/web.png'), '&exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)
        #List of users
        usersAction = QAction(QIcon('./images/web.png'), '&UserList', self)
        usersAction.setShortcut('Ctrl+U')
        usersAction.triggered.connect(self.getUsersList)
        #CreateUser
        CreateUser = QAction('&UserList', self)
        CreateUser.setShortcut('Ctrl+n')
        CreateUser.triggered.connect(self.CreateNewUser)
        fileMenu.addAction(exitAction)
        fileMenu2.addAction(usersAction)
        fileMenu2.addAction(CreateUser)
        #
        #Кнопка с всплывающей подсказкой
        #
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a push button')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        #---------------------------
        #Кнопка закрытия окна
        #---------------------------
        '''qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(10, 10)
        '''
        self.show()
    #--------------
    #Спросить действительно ли закрыть окно (по крестику)
    #--------------
    def closeEvent(self, event):  
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().right()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def getUsersList(self):
        tmpList = os.listdir()
        UsersList = []
        for item in tmpList:
            if item[-3:] == 'txt':
                UsersList.append(item)
        print(UsersList)
        x = 50
        y = 90
        for name in UsersList:
            namebtn = QPushButton(name, self)
            namebtn.move(x, y)
            y += 20

    def CreateNewUser(self):
        self.le = QLineEdit(self)
        self.le.move(70, 70)
        self.setWindowTitle("Create new user")
        self.show()
        text, ok = QInputDialog.getText(self, 'InputDialog', 'Enter new name: ')
        if ok:
            self.le.setText(str(text))
            NewName = self.le.getText()
        print(NewName)

#def CreateNewUser():
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


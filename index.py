import sys
import os
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


class InfoWindow(QMainWindow):
    def __init__(self, name, parent=None):                               
        super().__init__(parent)
        

        self.left, self.top, self.width, self.height = 400, 400, 300, 300

        self.name = name                                                  

        self.initUI()

    def initUI(self):
        self.setWindowTitle('info')

        self.infolabel = QLabel(self)                                     

        with open('{}.txt'.format(self.name), 'r') as f:    
            self.infolabel.setText(f.read())                              
            self.infolabel.adjustSize()                                   

        self.infolabel.setStyleSheet('border-style: solid; border-width: 1px; border-color: black; ')


class FirstWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.title = "Working time"
        self.left, self.top, self.width, self.height = 200, 200, 400, 400
        self.current = "none"

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('./images/TimeForWork.png'))
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu2 = menubar.addMenu('&Users')
        #Exit
        exitAction = QAction(QIcon('./images/web.png'), '&File', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.exit)
        #List of users
        usersAction = QAction(QIcon('./images/web.png'), '&UserList', self)
        usersAction.setShortcut('Ctrl+U')
        usersAction.triggered.connect(self.getUsersList)
        #CreateUser
        CreateUser = QAction('&CreateNew', self)
        CreateUser.setShortcut('Ctrl+n')
        CreateUser.triggered.connect(self.CreateNewUser)
        fileMenu.addAction(exitAction)
        fileMenu2.addAction(usersAction)
        fileMenu2.addAction(CreateUser)

        tmpList = os.listdir()
        UsersList = []
        for item in tmpList:
            if item[-3:] == 'txt':
                UsersList.append(item[:-4])

        self.combo = QComboBox(self)
        self.combo.addItem('Выберите сотрудника')
        self.combo.addItems(UsersList)
        self.combo.move(50, 50)
        self.combo.resize(200, 30)
        self.combo.activated[str].connect(self.onActivated)

    def winshow(self):
        self.info.show()  

    def onActivated(self, text):
        self.current = self.combo.currentText()
        if self.current != 'Выберите сотрудника':
            self.info = InfoWindow(self.current, self)                   

            self.winshow()

    def getUsersList(self):
        tmpList = os.listdir()
        UsersList = []
        for item in tmpList:
            if item[-3:] == 'txt':
                UsersList.append(item)
        print(UsersList)

    def CreateNewUser(self):
        self.le = QLineEdit(self)
        self.le.move(70, 70)
        self.setWindowTitle("Create new user")
        self.button = QPushButton("show", self)
        text, ok = QInputDialog.getText(self, 'InputDialog', 'Enter new name: ')
        print(text, ok)
        if text:                                          
            self.le.setText(text)                         
            NewName = self.le.text()                      
            with open('{}.txt'.format(text), 'w') as f:    
                pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            print('window closed')
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FirstWindow()
    ex.show()                                             
    sys.exit(app.exec_())

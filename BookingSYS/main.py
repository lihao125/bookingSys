import sys
import subprocess
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget
sys.path.append('./Boundary')
from loginUI import loginUI
from adminUI import adminUI

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the window properties
        self.resize(800,600)
        self.setWindowTitle('Main Page')

        #stackedwidget to move from page to page
        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        #main page
        self.layoutMain = QVBoxLayout()
        button = QPushButton('Admin')
        button.clicked.connect(self.adminLog)

        self.layoutMain.addWidget(QLabel('WHO ARE YOU!'))
        self.layoutMain.addWidget(button)

        self.pageMain = QWidget()
        self.pageMain.setLayout(self.layoutMain)
        self.stackedWidget.addWidget(self.pageMain)


        #login page from another class
        self.pageLogin = loginUI(self.stackedWidget)
        self.stackedWidget.addWidget(self.pageLogin)
        

    def adminLog(self):
        self.stackedWidget.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
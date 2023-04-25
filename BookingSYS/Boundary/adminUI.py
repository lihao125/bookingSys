import sys 
sys.path.append('./Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox, QListWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from manageAccController import manageAccController
from manageProfController import manageProfController

class adminUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget

        self.setWindowTitle('Admin')
        font = QtGui.QFont()
        font.setPointSize(16)
        

        # create the layout for main -----------------------------------
        layoutMain = QGridLayout()
        #Buttons
        self.pushButton1= QPushButton("Manage Accounts")
        self.pushButton2= QPushButton("Manage Profiles")

        self.pushButton1.clicked.connect(self.callMAcc)
        self.pushButton2.clicked.connect(self.callMProf)
        
        layoutMain.addWidget(self.pushButton1)
        layoutMain.addWidget(self.pushButton2)

        #-----------------------------------------------------------------
        self.setLayout(layoutMain)

    def mAcc(self):
        self.stackedWidget2.setCurrentIndex(1)

    def mProfile(self):
        self.stackedWidget2.setCurrentIndex(2)
        
    def callMAcc(self):
        manageAccController.manAcc(self, self.stackedWidget)

    def callMProf(self):
        manageProfController.manProf(self, self.stackedWidget)
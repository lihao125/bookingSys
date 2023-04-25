import sys 
#sys.path.append(r'C:\Users\Owner\Desktop\CSIT314\bookingSys\BookingSYS\Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
class adminUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
        self.stackedWidget2 = QStackedWidget()
        

        self.setWindowTitle('Admin')
        font = QtGui.QFont()
        font.setPointSize(16)
        

        # create the layout for main -----------------------------------
        layoutMain = QGridLayout()
        #Buttons
        self.pushButton1= QPushButton("Manage Accounts")
        self.pushButton2= QPushButton("Manage Profiles")

        self.pushButton1.clicked.connect(self.mAcc)
        self.pushButton2.clicked.connect(self.mProfile)
        
        layoutMain.addWidget(self.pushButton1)
        layoutMain.addWidget(self.pushButton2)

        #Stack 2 starting page
        layoutStart = QGridLayout()
        self.labelStart = QLabel ("Press one of the buttons to manage Accounts or Profiles")
        pageStart = QWidget()
        layoutStart.addWidget(self.labelStart)
        pageStart.setLayout(layoutStart)

        # layout for manage Accounts -----------------------------------
        layoutAcc = QGridLayout()
        pageAcc = QWidget()
        #Buttons
        self.pushButton11= QPushButton("In accounts")
        self.pushButton21= QPushButton("Manage Profiles")

        #self.pushButton1.clicked.connect(self.processHist)
        #self.pushButton2.clicked.connect(self.viewHist)
        
        layoutAcc.addWidget(self.pushButton11)
        layoutAcc.addWidget(self.pushButton21)
        pageAcc.setLayout(layoutAcc)

        # layout for manage profile-----------------------------------
        layoutProf = QGridLayout()
        pageProf = QWidget()
        #Buttons
        self.pushButton12= QPushButton("In profile")
        self.pushButton22= QPushButton("Manage Profiles")

        #self.pushButton1.clicked.connect(self.processHist)
        #self.pushButton2.clicked.connect(self.viewHist)
        
        layoutProf.addWidget(self.pushButton12)
        layoutProf.addWidget(self.pushButton22)
        pageProf.setLayout(layoutProf)


        # set the layout for the window to the stackedWidget
        self.stackedWidget2.addWidget(pageStart)
        self.stackedWidget2.addWidget(pageAcc)
        self.stackedWidget2.addWidget(pageProf)
        layoutMain.addWidget(self.stackedWidget2)

        #-----------------------------------------------------------------
        self.setLayout(layoutMain)
        self.stackedWidget2.setCurrentIndex(0)

    def mAcc(self):
        self.stackedWidget2.setCurrentIndex(1)

    def mProfile(self):
        self.stackedWidget2.setCurrentIndex(2)
        

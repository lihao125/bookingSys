import sys 
#sys.path.append(r'C:\Users\Owner\Desktop\CSIT314\bookingSys\BookingSYS\Controller')
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout, QMessageBox, QListWidget
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
        self.labelAcc= QLabel("In accounts")
        self.textBox1 = QListWidget()
        self.buttonCreate= QPushButton("Create Account")
        self.buttonDelete = QPushButton("Delete Account")
        self.buttonEdit = QPushButton("Edit Account")

        #self.pushButton1.clicked.connect(self.processHist)
        #self.pushButton2.clicked.connect(self.viewHist)
        
        layoutAcc.addWidget(self.textBox1,1 ,0 ,4 ,1)
        layoutAcc.addWidget(self.labelAcc,0,0)
        layoutAcc.addWidget(self.buttonCreate, 1 ,1)
        layoutAcc.addWidget(self.buttonDelete, 1 ,2)
        layoutAcc.addWidget(self.buttonEdit, 2 ,1)
        pageAcc.setLayout(layoutAcc)

        # layout for manage profile-----------------------------------
        layoutProf = QGridLayout()
        pageProf = QWidget()
        #Buttons
        self.labelProf= QLabel("In profiles")
        self.textBox2 = QListWidget()
        self.buttonCreate2= QPushButton("Create Profile")
        self.buttonDelete2 = QPushButton("Delete Profile")
        self.buttonEdit2 = QPushButton("Edit Profile")

        #self.pushButton1.clicked.connect(self.processHist)
        #self.pushButton2.clicked.connect(self.viewHist)
        
        layoutProf.addWidget(self.textBox2,1 ,0 ,4 ,1)
        layoutProf.addWidget(self.labelProf,0,0)
        layoutProf.addWidget(self.buttonCreate2, 1 ,1)
        layoutProf.addWidget(self.buttonDelete2, 1 ,2)
        layoutProf.addWidget(self.buttonEdit2, 2 ,1)
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
        

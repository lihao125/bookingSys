import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout
sys.path.append('./Boundary')
from manageAcc import manageAcc

class accManage:
    def fuc(self,stackedWidget):
        self.stackedWidget = stackedWidget
        print("in manageAcc")
        manage = manageAcc(self.stackedWidget)
        self.stackedWidget.addWidget(manage)
        self.stackedWidget.setCurrentIndex(3)

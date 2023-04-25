import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout
sys.path.append('./Boundary')
from manageProf import manageProf

class profManage:
    def fuc(self,stackedWidget):
        self.stackedWidget = stackedWidget
        print("in manageProf")
        manage = manageProf(self.stackedWidget)
        self.stackedWidget.addWidget(manage)
        self.stackedWidget.setCurrentIndex(4)
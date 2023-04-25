import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout

sys.path.append('./Boundary')
from adminUI import adminUI
class admin:
    def fuc(self,stackedWidget):
        self.stackedWidget = stackedWidget
        print("in staff")
        admin1 = adminUI(self.stackedWidget)
        self.stackedWidget.addWidget(admin1)
        self.stackedWidget.setCurrentIndex(2)

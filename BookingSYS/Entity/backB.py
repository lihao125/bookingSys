import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget, QGridLayout
sys.path.append('./Boundary')

class backB:
    def fuc(self,stackedWidget):
        self.stackedWidget = stackedWidget
        self.stackedWidget.setCurrentIndex(2)
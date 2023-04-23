import sys
import subprocess
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the window properties
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Main Page')

        layout = QVBoxLayout()

        button = QPushButton('Admin')
        button.clicked.connect(self.adminLog)

        layout.addWidget(QLabel('WHO ARE YOU!'))
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def adminLog(self):
        # Change directory to the directory containing the Python file you want to run
        # Replace the path with the actual path to your Python file
        subprocess.Popen(['python', 'C:/Users/USER/Desktop/BookingSys/bookingSys/bookingSYS/Boundary/adminLoginUI.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
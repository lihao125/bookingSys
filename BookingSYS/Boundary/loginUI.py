import sys 
sys.path.append('./Controller')
#sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Controller')
from adminLoginController import adminLoginController

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QStackedWidget


class loginUI(QWidget):
    def __init__(self, stackedWidget):
        super().__init__()

        self.stackedWidget = stackedWidget
    
        self.setWindowTitle('Login')

       # create the login form
        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        # create the layout
        layoutLogin = QVBoxLayout()
        layoutLogin.addWidget(self.username_label)
        layoutLogin.addWidget(self.username_edit)
        layoutLogin.addWidget(self.password_label)
        layoutLogin.addWidget(self.password_edit)
        layoutLogin.addWidget(self.login_button)

        # set the layout for the window to the stackedWidget
        self.setLayout(layoutLogin)

    def login(self):
        # get the username and password
        username = self.username_edit.text()
        password = self.password_edit.text()

        # do the login validation here
        if username == 'admin' and password == 'password':
            sd = adminLoginController.addStaff(self, self.stackedWidget)
        else:
            print('Login failed.')

import sys 
sys.path.append('C:/Users/USER/Desktop/BookingSys/bookingSys/BookingSYS/Controller')
from adminLoginController import adminLoginController

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # set the window properties
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Admin Login')

       # create the login form
        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login)

        # create the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.username_label)
        vbox.addWidget(self.username_edit)
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_edit)
        vbox.addWidget(self.login_button)

        # set the layout for the window
        self.setLayout(vbox)

    def login(self):
        # get the username and password
        username = self.username_edit.text()
        password = self.password_edit.text()

        # do the login validation here
        if username == 'admin' and password == 'password':
            admin1 = adminLoginController()
            sd = adminLoginController.addStaff(self)
        else:
            print('Login failed.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
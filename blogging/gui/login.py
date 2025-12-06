from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QApplication
from blogging.configuration import Configuration
from blogging.controller import Controller

class loginGui(QWidget):
    ''' the login gui'''
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        label_username = QLabel("Username")
        self.text_username = QLineEdit()
        label_password = QLabel("Password")
        self.text_password = QLineEdit()
        self.text_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.button_login = QPushButton("Login")
        self.button_quit = QPushButton("Quit")

        layout.addWidget(label_username, 0, 0)
        layout.addWidget(self.text_username, 0, 1)
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.text_password, 1, 1)
        layout.addWidget(self.button_login, 2, 0)
        layout.addWidget(self.button_quit, 2, 1)

        self.setLayout(layout)

        self.button_login.clicked.connect(self.login_pressed)
        self.button_quit.clicked.connect(self.quit_pressed)

    def login_pressed(self):
        '''gets data from the '''
        username = self.text_username.text()
        password = self.text_password.text()

        controller = self.main_window.controller

        try:
            controller.login(username, password)
            self.main_window.switchGui("blog_menu")
        except:
            msg = QMessageBox()
            msg.setText("Wrong username/password")

            msg.exec()        

            self.text_username.setText('')
            self.text_password.setText('')
    
    def quit_pressed(self):
        '''close the application'''
        QApplication.instance().quit()
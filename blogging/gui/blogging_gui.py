import sys
from blogging.configuration import Configuration
from blogging.controller import Controller
from .login import loginGui
from .logged_in import loggedInGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt6.QtGui import QIcon

class BloggingGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        self.controller = Controller()
        self.setWindowIcon(QIcon("uvic.png"))

        self.view_map = {
            "login" : 0,
            "logged_in" : 1
        }
 
        self.widget= QStackedWidget()
        self.widget.addWidget(loginGui(self))
        self.widget.addWidget(loggedInGui(self))
        
        self.setCentralWidget(self.widget)
        self.switchGui("login")
    
    def switchGui(self, index):
        self.widget.setCurrentIndex(self.view_map[index])


def main():
    app = QApplication(sys.argv)
    window = BloggingGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()

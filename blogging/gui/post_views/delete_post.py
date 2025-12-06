from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller

class deletePost(QWidget):
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        self.button_back = QPushButton("Back")

        layout.addWidget(self.button_back,       3, 0)

        self.button_back.clicked.connect(
            lambda: self.main_window.switchGui("post_menu")
        )

        self.setLayout(layout)
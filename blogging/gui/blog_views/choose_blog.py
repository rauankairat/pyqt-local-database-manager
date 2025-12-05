from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller

class chooseBlog(QWidget):
    def __init__(self, main_win):
        super().__init__()
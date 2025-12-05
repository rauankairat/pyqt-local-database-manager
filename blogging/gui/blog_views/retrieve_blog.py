from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller

class retrieveBlog(QWidget):
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        label_id = QLabel("ID")
        self.text_id = QLineEdit()
        self.back_btn = QPushButton("back")
        self.retrieve_btn = QPushButton("retrieve")

        label_name = QLabel("name:")
        label_url = QLabel("url:")
        label_email = QLabel("email:")
        label_post_count = QLabel("post count:")

        self.name_line = QLineEdit("")
        self.url_line = QLineEdit("")
        self.email_line = QLineEdit("")
        self.post_count_line = QLineEdit("")


        self.retrieve_btn.clicked.connect(self.retrieve)
        self.back_btn.clicked.connect(self.back)

        self.setLayout(layout)
    
    def retrieve(self):
        cont = self.main_window.controller

        try:
            pass

        except BaseException as e:
            msg = QMessageBox()
            msg.setText(e.__doc__)

            msg.exec()
    
    def back(self):
        self.main_window.switchGui("blog_menu")
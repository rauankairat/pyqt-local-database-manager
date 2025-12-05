from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout, QApplication
from blogging.configuration import Configuration
from blogging.controller import Controller

from ..post_menu import postMenu

class chooseBlog(QWidget):
    def __init__(self, main_win):
        super().__init__()

        self.configuration = Configuration()
        self.configuration.__class__.autosave = True

        self.main_window=main_win

        layout = QGridLayout()

        label_id = QLabel("ID")
        self.text_id = QLineEdit()
        self.back_btn = QPushButton("back")
        self.search_btn = QPushButton("search")


        self.name_line = QLineEdit("")
        self.url_line = QLineEdit("")
        self.email_line = QLineEdit("")
        self.post_count_line = QLineEdit("")

        layout.addWidget(label_id,        0, 0)
        layout.addWidget(self.text_id,    0, 1)

        layout.addWidget(self.back_btn, 1, 0)
        layout.addWidget(self.search_btn,  1, 1)

        self.search_btn.clicked.connect(self.search)
        self.back_btn.clicked.connect(self.back)

        self.setLayout(layout)
    
    def search(self):
        id = self.text_id.text()

        cont = self.main_window.controller

        result = cont.search_blog(id)

        if result != None:

            cont.current_blog = result   
            self.main_window.switchGui("post_menu")
            
            
        else:
            msg = QMessageBox()
            msg.setText("Not found")

            msg.exec()
    
    def back(self):
        self.main_window.switchGui("blog_menu")
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller

class createBlog(QWidget):
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        self.back_btn = QPushButton("back")
        self.create_btn = QPushButton("create")

        label_id = QLabel("ID:")
        label_name = QLabel("name:")
        label_url = QLabel("url:")
        label_email = QLabel("email:")

        self.id_edit = QLineEdit("")
        self.name_edit = QLineEdit("")
        self.url_edit = QLineEdit("")
        self.email_edit = QLineEdit("")

        layout.addWidget(label_id,        0, 0)
        layout.addWidget(self.id_edit,    0, 1)

        layout.addWidget(label_name,        1, 0)
        layout.addWidget(self.name_edit,   1, 1)

        layout.addWidget(label_url,         2, 0)
        layout.addWidget(self.url_edit,    2, 1)

        layout.addWidget(label_email,       3, 0)
        layout.addWidget(self.email_edit,  3, 1)

        layout.addWidget(self.back_btn,  4,0)
        layout.addWidget(self.create_btn,4,1)

        self.create_btn.clicked.connect(self.create)
        self.back_btn.clicked.connect(self.back)

        self.setLayout(layout)
    
    def create(self):
        id = self.id_edit.text()
        name = self.name_edit.text()
        url = self.url_edit.text()
        email = self.email_edit.text()

        cont = self.main_window.controller

        try:
            result = cont.create_blog(int(id),name,url,email)
            msg = QMessageBox()
            msg.setText("successfully created blog")

            msg.exec()

        except BaseException as e:
            msg = QMessageBox()
            msg.setText(e.__doc__)

            msg.exec()
    
    def back(self):
        self.main_window.switchGui("blog_menu")
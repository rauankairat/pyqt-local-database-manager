from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtCore import Qt
from blogging.configuration import Configuration
from blogging.controller import Controller

class createPost(QWidget):
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()


        label_tittle = QLabel("Tittle:")
        label_text = QLabel("Text:")


        self.tittle_edit = QLineEdit("")
        
        self.text_edit = QLineEdit("")
        self.text_edit.setFixedHeight(100)
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.button_back = QPushButton("Back")
        self.button_create = QPushButton("Create")




        layout.addWidget(label_tittle,        1, 0)
        layout.addWidget(self.tittle_edit,   1, 1)

        layout.addWidget(label_text,         2, 0)
        layout.addWidget(self.text_edit,    2, 1)

        layout.addWidget(self.button_back,       3, 0)
        layout.addWidget(self.button_create,       3, 1)
  
     


        self.button_back.clicked.connect(
            lambda: self.main_window.switchGui("post_menu")
        )
        
        self.button_create.clicked.connect(self.create)

        self.setLayout(layout)


    def create(self):
        tittle = self.tittle_edit.text()
        text = self.text_edit.text()

        cont = self.main_window.controller

        try:
            result = cont.create_post(tittle,text)
            msg = QMessageBox()
            msg.setText("Successfully created post")

            msg.exec()

        except BaseException as e:
            msg = QMessageBox()
            msg.setText(str(e))
            msg.exec()






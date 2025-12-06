from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller

class updatePost(QWidget):
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        self.button_back = QPushButton("Back")
        self.button_update = QPushButton("Update")

        label_code = QLabel("code:")
        label_tittle = QLabel("Tittle:")
        label_text = QLabel("Text:")


        self.code_edit = QLineEdit("")
        self.tittle_edit = QLineEdit("")
        self.text_edit = QLineEdit("")


        layout.addWidget(label_code,     0, 0)
        layout.addWidget(self.code_edit,    0, 1)

        layout.addWidget(label_tittle,        1, 0)
        layout.addWidget(self.tittle_edit,   1, 1)

        layout.addWidget(label_text,         2, 0)
        layout.addWidget(self.text_edit,    2, 1)

        layout.addWidget(self.button_back,    3, 0)
        layout.addWidget(self.button_update,    3, 1)


        self.button_back.clicked.connect(
            lambda: self.main_window.switchGui("post_menu")
        )

        self.button_update.clicked.connect(self.update)

        self.setLayout(layout)

    def update(self):
        code = self.code_edit.text()
        tittle = self.tittle_edit.text()
        text = self.text_edit.text()
        
        cont = self.main_window.controller
        
        try:
            

            result = cont.update_post(code,tittle,text)
            msg = QMessageBox()
            msg.setText("Successfully created post")

            msg.exec()
        
        except BaseException as e:
            msg = QMessageBox()
            msg.setText(str(e))
            msg.exec()

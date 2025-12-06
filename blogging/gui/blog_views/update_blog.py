from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller

class updateBlog(QWidget):
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        label_id = QLabel("id:")
        self.prev_id = QLineEdit()
        self.search_btn = QPushButton("search")

        label_new_id = QLabel("new id:")
        label_name = QLabel("name:")
        label_url = QLabel("url:")
        label_email = QLabel("email:")

        self.back_btn = QPushButton("back")
        self.update_btn = QPushButton("update")

        self.id_line = QLineEdit("")
        self.name_line = QLineEdit("")
        self.url_line = QLineEdit("")
        self.email_line = QLineEdit("")

        layout.addWidget(label_id,        0, 0)
        layout.addWidget(self.prev_id,    0, 1)

        layout.addWidget(self.search_btn,  1, 0, 1,2)

        layout.addWidget(label_new_id, 2, 0)
        layout.addWidget(self.id_line, 2, 1)

        layout.addWidget(label_name, 3, 0)
        layout.addWidget(self.name_line, 3, 1)

        layout.addWidget(label_url, 4, 0)
        layout.addWidget(self.url_line, 4, 1)

        layout.addWidget(label_email, 5, 0)
        layout.addWidget(self.email_line, 5, 1)

        layout.addWidget(self.back_btn, 6, 0)
        layout.addWidget(self.update_btn, 6, 1)


        self.search_btn.clicked.connect(self.search)
        self.back_btn.clicked.connect(self.back)
        self.update_btn.clicked.connect(self.update)


        self.setLayout(layout)
    
    def search(self):
        id = self.prev_id.text()

        cont = self.main_window.controller

        result = cont.search_blog(int(id))

        if result != None:
            self.id_line.setText(str(result.id))
            self.name_line.setText(str(result.name))
            self.url_line.setText(str(result.url))
            self.email_line.setText(str(result.email))
        else:
            msg = QMessageBox()
            msg.setText("Not found")

            msg.exec()

    def update(self):
        ''' delegates to controllers'''
        id = self.id_line.text()
        name = self.name_line.text()
        url = self.url_line.text()
        email = self.email_line.text()

        cont = self.main_window.controller

        try:
            cont.update_blog(int(self.prev_id.text()), int(id),name,url,email)
            msg = QMessageBox()
            msg.setText("successfully updated blog")
            msg.exec()
        except BaseException as e:
            msg = QMessageBox()
            msg.setText(e.__doc__)
            msg.exec()
    
    def back(self):
        self.main_window.switchGui("blog_menu")
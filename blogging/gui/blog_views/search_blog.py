from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller

class searchBlog(QWidget):
    ''' search blog view '''
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

        label_name = QLabel("name:")
        label_url = QLabel("url:")
        label_email = QLabel("email:")
        label_post_count = QLabel("post count:")

        self.name_line = QLineEdit("")
        self.url_line = QLineEdit("")
        self.email_line = QLineEdit("")
        self.post_count_line = QLineEdit("")

        layout.addWidget(label_id,        0, 0)
        layout.addWidget(self.text_id,    0, 1)

        layout.addWidget(self.back_btn, 1, 0)
        layout.addWidget(self.search_btn,  1, 1)

        layout.addWidget(label_name, 2, 0)
        layout.addWidget(self.name_line,        2, 1)

        layout.addWidget(label_url, 3, 0)
        layout.addWidget(self.url_line,         3, 1)

        layout.addWidget(label_email, 4, 0)
        layout.addWidget(self.email_line,       4, 1)

        layout.addWidget(label_post_count, 5,0)
        layout.addWidget(self.post_count_line,  5, 1)

        self.search_btn.clicked.connect(self.search)
        self.back_btn.clicked.connect(self.back)

        self.setLayout(layout)
    
    def search(self):
        '''delegates to search_blog'''
        id = self.text_id.text()

        cont = self.main_window.controller

        result = cont.search_blog(int(id))

        if result != None:
            self.name_line.setText(str(result.name))
            self.url_line.setText(str(result.url))
            self.email_line.setText(str(result.email))
            self.post_count_line.setText(str(result.post_count))
        else:
            msg = QMessageBox()
            msg.setText("Not found")

            msg.exec()
    
    def back(self):
        self.main_window.switchGui("blog_menu")
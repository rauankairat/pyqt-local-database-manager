from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller



class postMenu(QWidget):
    def __init__(self, main_win):
        """
            Post menu for options to do with posts in curent blog
        """
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()


        self.button_create = QPushButton("Create Post")
        self.button_retrieve = QPushButton("Retrieve Posts")
        self.button_update = QPushButton("Update Post")
        self.button_delete = QPushButton("Delete Post")
        self.button_list = QPushButton("List Posts")
        self.button_back = QPushButton("Back")
    
        self.button_logout = QPushButton("Log out")

        layout.addWidget(self.button_create,   0, 0)
        layout.addWidget(self.button_retrieve,   1, 0)
        layout.addWidget(self.button_update, 2, 0)
        layout.addWidget(self.button_delete,   3, 0)
        layout.addWidget(self.button_list,   4, 0)
        layout.addWidget(self.button_back,   5, 0)
        layout.addWidget(self.button_logout,     6, 0)
      

        
        self.button_create.clicked.connect(
            lambda: self.main_window.switchGui("create_post")
        )
        self.button_retrieve.clicked.connect(
            lambda: self.main_window.switchGui("retrieve_posts")
        )
        self.button_update.clicked.connect(
            lambda: self.main_window.switchGui("update_post")
        )
        self.button_delete.clicked.connect(
            lambda: self.main_window.switchGui("delete_post")
        )
        self.button_list.clicked.connect(
            lambda: self.main_window.switchGui("list_posts")
        )

        self.button_back.clicked.connect(
            lambda: self.main_window.switchGui("choose_blog")
        )
       
        self.button_logout.clicked.connect(
            lambda: self.main_window.switchGui("logout")
        )

        self.setLayout(layout)
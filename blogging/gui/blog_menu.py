from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller

class blogMenu(QWidget):
    '''
    main view shown after the login view.
    all views accessed by this menu have the same structure:
    - a class containing the views with the widgets in the __init__
    - one or two functions to get the data from to widgets and call the controller methods with them
    - a back function to return to this menu
    '''
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        self.button_search = QPushButton("Search Blogs")
        self.button_create = QPushButton("Create Blog")
        self.button_retrieve = QPushButton("Retrieve Blogs")
        self.button_update = QPushButton("Update Blog")
        self.button_delete = QPushButton("Delete Blog")
        self.button_list = QPushButton("List Blogs")
        self.button_choose = QPushButton("Choose Blog")
        self.button_logout = QPushButton("Log out")

        # add widgets to the layout
        layout.addWidget(self.button_search,   0, 0)
        layout.addWidget(self.button_create,   1, 0)
        layout.addWidget(self.button_retrieve, 2, 0)
        layout.addWidget(self.button_update,   3, 0)
        layout.addWidget(self.button_delete,   4, 0)
        layout.addWidget(self.button_list,     5, 0)
        layout.addWidget(self.button_choose,   6, 0)
        layout.addWidget(self.button_logout,   7, 0)

        # connect the buttons to a switchGui call
        self.button_search.clicked.connect(
            lambda: self.main_window.switchGui("search_blogs")
        )
        self.button_create.clicked.connect(
            lambda: self.main_window.switchGui("create_blog")
        )
        self.button_retrieve.clicked.connect(
            lambda: self.main_window.switchGui("retrieve_blogs")
        )
        self.button_update.clicked.connect(
            lambda: self.main_window.switchGui("update_blog")
        )
        self.button_delete.clicked.connect(
            lambda: self.main_window.switchGui("delete_blog")
        )
        self.button_list.clicked.connect(
            lambda: self.main_window.switchGui("list_blogs")
        )
        self.button_choose.clicked.connect(
            lambda: self.main_window.switchGui("choose_blog")
        )
        self.button_logout.clicked.connect(
            lambda: self.main_window.switchGui("logout")
        )

        self.setLayout(layout)
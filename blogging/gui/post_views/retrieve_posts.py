from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTableView
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller
from .post_table_view import PostTableModel

class retrievePosts(QWidget):
    """
        List all blogs containg typed tittle or text in current blog 
    """
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        tittle_label = QLabel('Tittle or Text:')
        self.tittle = QLineEdit()
        self.back_btn = QPushButton("back")
        self.retrieve_btn = QPushButton("retrieve")

        self.table = QTableView()

        layout.addWidget(tittle_label, 0,0)
        layout.addWidget(self.tittle,0,1)
        layout.addWidget(self.back_btn, 1,0)
        layout.addWidget(self.retrieve_btn, 1,1)
        layout.addWidget(self.table, 2, 0, 1, 2)

        self.retrieve_btn.clicked.connect(self.retrieve)
        self.back_btn.clicked.connect(self.back)

        self.setLayout(layout)
    
    def retrieve(self):
        cont = self.main_window.controller
        
        tittle = self.tittle.text()

        try:
            result = cont.retrieve_posts(tittle)
            self.table.setModel(PostTableModel(result))
        except BaseException as e:
            msg = QMessageBox()
            msg.setText(e.__doc__)
            msg.exec()
    
    def back(self):
        self.main_window.switchGui("post_menu")
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTableView
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller
from .post_table_view import PostTableModel

class listPosts(QWidget):
    """
        List posts in current blog
    """
    def __init__(self, main_win):
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window=main_win

        layout = QGridLayout()

        self.back_btn = QPushButton("back")
        self.reload_btn = QPushButton("reload")

        self.table = QTableView()

        layout.addWidget(self.table, 0, 0)
        layout.addWidget(self.reload_btn, 1,0)
        layout.addWidget(self.back_btn, 2,0)


        self.reload_btn.clicked.connect(self.reload)
        self.back_btn.clicked.connect(self.back)

        self.setLayout(layout)

       
    def showEvent(self, event):
        super().showEvent(event)
        self.reload()


    def reload(self):
         
        cont = self.main_window.controller

        try:
            result = cont.list_posts()
            self.table.setModel(PostTableModel(result))
        except BaseException as e:
            msg = QMessageBox()
            msg.setText(str(e))
            msg.exec()
    
    def back(self):
        self.main_window.switchGui("post_menu")
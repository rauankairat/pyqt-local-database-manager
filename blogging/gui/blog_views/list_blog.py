from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTableView
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration
from blogging.controller import Controller
from .blog_table_view import BlogTableModel

class listBlog(QWidget):
    '''lists the blogs in a view'''
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
    
    def reload(self):
        ''' since the stack wouldnt update the component on switching the view, i added a reload button instead'''
        cont = self.main_window.controller

        try:
            result = cont.list_blogs()
            self.table.setModel(BlogTableModel(result))
        except BaseException as e:
            msg = QMessageBox()
            msg.setText(e.__doc__)
            msg.exec()
    
    def back(self):
        self.main_window.switchGui("blog_menu")
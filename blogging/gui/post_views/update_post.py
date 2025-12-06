from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtWidgets import QGridLayout
from blogging.configuration import Configuration

class updatePost(QWidget):
    def __init__(self, main_win):
        """
            Update post by searching by its code and changing text and tittle in curent blog.
        """
        super().__init__()
        
        self.configuration = Configuration()
        self.configuration.__class__.autosave = True
        
        self.main_window = main_win

        layout = QGridLayout()

        self.button_back = QPushButton("Back")
        self.button_update = QPushButton("Update")
        self.button_search = QPushButton("Search")

        label_code = QLabel("Code:")
        self.code_edit = QLineEdit("")

        label_new_title = QLabel("New Title:")
        label_new_text = QLabel("New Text:")

        self.new_tittle_edit = QLineEdit("")
        self.new_text_edit = QLineEdit("")

        layout.addWidget(label_code, 0, 0)
        layout.addWidget(self.code_edit, 0, 1)
        layout.addWidget(self.button_search, 1, 1)

        layout.addWidget(label_new_title, 3, 0)
        layout.addWidget(self.new_tittle_edit, 3, 1)

        layout.addWidget(label_new_text, 4, 0)
        layout.addWidget(self.new_text_edit, 4, 1)

        layout.addWidget(self.button_back, 5, 0)
        layout.addWidget(self.button_update, 5, 1)

        self.button_search.clicked.connect(self.search)
        self.button_back.clicked.connect(lambda: self.main_window.switchGui("post_menu"))
        self.button_update.clicked.connect(self.update)

        self.setLayout(layout)

    def search(self):
        code = int(self.code_edit.text())
        cont = self.main_window.controller

        result = cont.search_post(code)

        if result is not None:
            self.new_tittle_edit.setText(result.title)
            self.new_text_edit.setText(result.text)
        else:
            QMessageBox.warning(self, "Error", "Post not found")

    def update(self):
        code = int(self.code_edit.text())
        tittle = self.new_tittle_edit.text()
        text = self.new_text_edit.text()

        cont = self.main_window.controller

        try:
            cont.update_post(code, tittle, text)
            QMessageBox.information(self, "Success", "Successfully updated post")
        except BaseException as e:
            QMessageBox.warning(self, "Error", str(e))

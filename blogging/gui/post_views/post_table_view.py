from PyQt6 import QtCore
from PyQt6.QtCore import Qt

class PostTableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        """
        Table for list posts and retrive posts
        """
        
        super().__init__()
        self._data = data  # list of Post objects

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            post = self._data[index.row()]

            if index.column() == 0:
                return post.code
            elif index.column() == 1:
                return post.title
            elif index.column() == 2:
                return post.text

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return 3  # code, title, text

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            if section == 0:
                return "Code"
            elif section == 1:
                return "Title"
            elif section == 2:
                return "Text"
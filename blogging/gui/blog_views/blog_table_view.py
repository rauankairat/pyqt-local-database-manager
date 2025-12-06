
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt


class BlogTableModel(QtCore.QAbstractTableModel):
    '''model of blogs for QTableView'''
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column()==0:
                return self._data[index.row()].id
            elif index.column()==1:
                return self._data[index.row()].name
            elif index.column()==2:
                return self._data[index.row()].url
            elif index.column()==3:
                return self._data[index.row()].email

    def rowCount(self, index):

        return len(self._data)

    def columnCount(self, index):
        return 4
    
    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            if section == 0:
                return "Id"
            elif section == 1:
                return "Name"
            elif section == 2:
                return "url"
            elif section == 3:
                return "email"
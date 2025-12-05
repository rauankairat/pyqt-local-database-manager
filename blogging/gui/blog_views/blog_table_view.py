class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            if index.column()==0:
                return self._data[index.row()].id
            elif index.column()==1:
                return self._data[index.row()].name
            elif index.column()==2:
                return self._data[index.row()].url
            elif index.column()==3:
                return self._data[index.row()].email

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        return 4
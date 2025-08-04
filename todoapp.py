import json
import os.path
import sys

from PySide6.QtWidgets import QStyle

from resources.forms.todo import *
from PySide6.QtCore import QAbstractListModel, Qt, QEvent


class TodoModel(QAbstractListModel):
    def __init__(self, todo_list=None):
        super(TodoModel, self).__init__()
        self.todo_list = todo_list or list()

    def rowCount(self, parent=None):
        return len(self.todo_list)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            status, text = self.todo_list[index.row()]
            return text

        if role == Qt.ItemDataRole.DecorationRole:
            status, text = self.todo_list[index.row()]
            style = QApplication.style()
            if status:
                return style.standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton)
            else:
                return style.standardIcon(QStyle.StandardPixmap.SP_DialogCancelButton)

        return None


class Todo(QWidget, Ui_Form):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.data_file = os.path.join(os.path.dirname(__file__), 'data.json')
        self.load()
        self.list_view.setModel(self.model)
        self.mainwindow = mainwindow

        self.add_btn.clicked.connect(self.add)
        self.delete_btn.clicked.connect(self.delete)
        self.complete_btn.clicked.connect(self.complete)

        self.list_view.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.list_view.installEventFilter(self)

    def add(self):
        if self.line_edit.text():
            self.model.todo_list.append((False, self.line_edit.text()))
            self.model.layoutChanged.emit()
            self.line_edit.clear()
            self.save()

    def keyPressEvent(self, event, /):
        if self.line_edit.hasFocus():
            if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
                self.add()

    def eventFilter(self, obj, event):
        if obj == self.list_view and event.type() == QEvent.Type.KeyPress and event.key() == Qt.Key.Key_Q:
            if self.mainwindow:
                self.hide()
                self.mainwindow.show()
            else:
                self.close()
            return True
        return False

    def delete(self):
        if self.list_view.selectedIndexes() and self.model.todo_list:
            index = self.list_view.selectedIndexes()[0]
            self.model.todo_list.pop(index.row())
            self.model.layoutChanged.emit()
            self.save()

    def complete(self):
        if self.list_view.selectedIndexes() and self.model.todo_list:
            index = self.list_view.selectedIndexes()[0]
            status, text = self.model.todo_list[index.row()]
            self.model.todo_list[index.row()] = True, text
            self.model.dataChanged.emit(index, index, self.model.todo_list)
            self.save()

    def load(self):
        try:
            with open(self.data_file, 'r') as f:
                self.model.todo_list = json.load(f)
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.model.todo_list, f)

    def closeEvent(self, event, /):
        if self.isVisible():
            self.mainwindow.show()
            event.accept()
        super().closeEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Todo()
    window.show()
    sys.exit(app.exec())

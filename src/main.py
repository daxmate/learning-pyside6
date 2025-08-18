import sys

from PySide6.QtCore import Qt, QAbstractListModel
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               )

from helloworld import HelloWorld
from layouts import Layouts
from signal_and_slot import SignalAndSlot
from src.guess_number import GuessNumber
from todoapp import Todo
from widget_gallery import WidgetGallery
from mainwindow import Ui_MainWindow


class LessonModel(QAbstractListModel):
    def __init__(self, lessons=None):
        super().__init__()
        self.lessons = lessons or []

    def rowCount(self, parent=None):
        return len(self.lessons)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self.lessons[index.row()]
        return None


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = LessonModel()
        self.listView.setModel(self.model)
        self.widget = None
        self.lessons = [
            ("Hello World", HelloWorld),
            ("布局", Layouts),
            ("信号与槽", SignalAndSlot),
            ("猜数字", GuessNumber),
            ("待办事项小应用", Todo),
            ("常用控件库", WidgetGallery),
        ]
        self.add_lessons()

    def add_lessons(self):
        for index, (title, _) in enumerate(self.lessons):
            self.model.lessons.append(f'第{index + 1}课. {title}')
            self.model.layoutChanged.emit()
        self.listView.clicked.connect(self.on_list_view_clicked)

    def on_list_view_clicked(self, index):
        self.widget = self.lessons[index.row()][1](self)
        self.widget.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("""
            QListView {
                border: 1px solid #ccc;
                font-size: 16px;
            }

            QListView::item {
                padding: 8px;
                border-bottom: 1px solid #eee;
            }

            QListView::item:hover {
                background-color: #e0f7fa;
                color: #00796b;
            }

            QListView::item:selected {
                background-color: #b2ebf2;
                color: #004d40;
            }
        """)
    window.show()
    sys.exit(app.exec())

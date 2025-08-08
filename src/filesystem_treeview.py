from PySide6.QtWidgets import (
    QTreeView,
    QFileSystemModel,
    QMenu
)
from PySide6.QtCore import QDir
from PySide6.QtGui import QAction
import os
import sys


class FileSystemTreeView(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_system_model = QFileSystemModel()
        home_path = QDir().homePath()
        self.file_system_model.setRootPath(home_path)

        self.setModel(self.file_system_model)
        self.hideColumn(2)
        self.setRootIndex(self.file_system_model.index(home_path))
        self.doubleClicked.connect(self.open_file)

        self.context_menu = QMenu()

    def open_file(self):
        file_path = self.file_system_model.filePath(self.currentIndex())
        if os.path.isfile(file_path):
            os.system(f'open {file_path}')
        else:
            if not self.isExpanded(self.currentIndex()):
                self.expand(self.currentIndex())

    def reveal_in_finder(self):
        path = self.file_system_model.filePath(self.currentIndex())
        if sys.platform == 'darwin':
            os.system(f'open -R {path}')

    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction("打开", self.open_file)
        menu.addAction("在Finder中显示", self.reveal_in_finder)

        menu.exec(event.globalPos())

        event.accept()

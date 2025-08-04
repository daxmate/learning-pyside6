from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QListView,
    QPushButton,
)

from PySide6.QtCore import (
    Qt, QEvent,
)

import sys


class KeypressWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.list_view = QListView()
        layout.addWidget(self.list_view)

        self.setLayout(layout)
        self.list_view.installEventFilter(self)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Q:
            self.close()

    def eventFilter(self, watched, event, /):
        if watched == self.list_view and event.type() == QEvent.Type.KeyPress:
            if event.key() == Qt.Key.Key_Q:
                self.close()
            return True
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KeypressWindow()
    window.show()
    sys.exit(app.exec())

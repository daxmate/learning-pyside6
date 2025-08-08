from PySide6.QtWidgets import QWidget


class DWidget(QWidget):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.mainwindow = mainwindow

    def closeEvent(self, event, /):
        if self.mainwindow and not self.mainwindow.isVisible():
            self.mainwindow.show()
        event.accept()

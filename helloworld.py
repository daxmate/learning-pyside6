from IPython.testing.tools import help_output_test
from PyQt6.QtWidgets import QApplication, QWidget
import sys


class HelloWorld(QWidget):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.resize(600, 300)
        self.setWindowTitle("Hello World")
        self.center()

    def center(self):
        screen_center = self.screen().availableGeometry().center()
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screen_center)
        self.geometry()

    def closeEvent(self, event):
        if not self.mainwindow.isVisible():
            self.mainwindow.show()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWorld()
    window.show()
    sys.exit(app.exec())

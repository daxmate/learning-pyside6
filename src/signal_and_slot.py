import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import Slot, Signal
from dax import DWidget
from src.forms.signal_and_slot import Ui_widget


class SignalAndSlot(DWidget, Ui_widget):
    def __init__(self, mainwindow=None):
        super().__init__(mainwindow)
        self.setupUi(self)
        self.step = 100
        for button in [self.up_btn, self.down_btn, self.left_btn, self.right_btn]:
            button.clicked.connect(self.move_window)

    def move_window(self):
        screen = self.screen().availableGeometry()
        frame = self.frameGeometry()
        if self.sender() == self.up_btn:
            self.move(self.x(), max(self.y() - self.step, 0))
        elif self.sender() == self.down_btn:
            self.move(self.x(), min(self.y() + self.step, screen.bottom() - frame.height()))
        elif self.sender() == self.left_btn:
            self.move(max(0, self.x() - self.step), self.y())
        elif self.sender() == self.right_btn:
            self.move(min(screen.right() - frame.width(), self.x() + self.step), self.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignalAndSlot()
    window.show()
    sys.exit(app.exec())

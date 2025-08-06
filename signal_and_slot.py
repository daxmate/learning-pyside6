import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import Slot, Signal
from dax import DWidget


class SignalAndSlot(DWidget):
    def __init__(self, mainwindow=None):
        super().__init__(mainwindow)
        self.label = QLabel("初始文本", self)
        self.button = QPushButton("点击我……", self)
        self.layout = QHBoxLayout(self)
        self.init_ui()

    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("信号与槽")
        self.resize(800, 600)
        center = self.screen().availableGeometry().center()
        self.geometry().moveCenter(center)

        # 添加控件到布局
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        # 链接信号与槽
        self.button.clicked.connect(self.update_label)

    @Slot()
    def update_label(self):
        self.label.setText("文本已更新")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignalAndSlot()
    window.show()
    sys.exit(app.exec())

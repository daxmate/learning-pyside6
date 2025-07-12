import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSpacerItem, \
    QSizePolicy

from helloworld import HelloWorld
from layouts import Layouts


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.centralWidget = QWidget()
        self.helloworld = None
        self.layouts = None
        self.init_ui()

    def init_ui(self):
        self.resize(300, 600)
        self.setWindowTitle("PyQt6教程")
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.layout)
        screen_center = self.screen().availableGeometry().center()
        self.frameGeometry().moveCenter(screen_center)

        self.add_buttons()

        self.layout.addItem(QSpacerItem(300, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))

    def add_buttons(self):
        helloworld_btn = QPushButton("第1课 Hello World")
        helloworld_btn.clicked.connect(self.open_helloworld)
        helloworld_btn.setObjectName("helloworld")
        layouts_btn = QPushButton("第2课 布局")
        layouts_btn.clicked.connect(self.open_layouts)
        self.layout.addWidget(helloworld_btn)
        self.layout.addWidget(layouts_btn)

        self.set_button_text_alignment()

    def set_button_text_alignment(self):
        for index in range(self.layout.count()):
            item = self.layout.itemAt(index)
            if item is not None:
                widget = item.widget()
                if isinstance(widget, QPushButton):
                    widget.setStyleSheet('text-align: left;')

    def open_helloworld(self):
        if self.helloworld is None:
            self.helloworld = HelloWorld(self)
        self.helloworld.show()
        self.hide()

    def open_layouts(self):
        if self.layouts is None:
            self.layouts = Layouts(self)
        self.layouts.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'resources', 'icons'))

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSpacerItem, \
    QSizePolicy

from helloworld import HelloWorld
from layouts import Layouts
from signal_and_slot import SignalAndSlot
from todoapp import Todo
from widget_gallery import WidgetGallery


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.centralWidget = QWidget()
        self.helloworld = None
        self.layouts = None
        self.signal_and_slot = None
        self.todoapp = None
        self.widget_gallery = None
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
        helloworld_btn = QPushButton("第1课 Hello World", flat=True)
        helloworld_btn.clicked.connect(self.open_helloworld)
        helloworld_btn.setObjectName("helloworld")

        layouts_btn = QPushButton("第2课 布局", flat=True)
        layouts_btn.clicked.connect(self.open_layouts)

        signal_and_slot_btn = QPushButton("第3课 信号与槽", flat=True)
        signal_and_slot_btn.clicked.connect(self.open_signal_and_slot)

        todo_btn = QPushButton("第4课 Todo App", flat=True)
        todo_btn.clicked.connect(self.open_todoapp)

        gallery_btn = QPushButton("第5课 常用控件", flat=True)
        gallery_btn.clicked.connect(self.open_widget_gallery)

        self.layout.addWidget(helloworld_btn)
        self.layout.addWidget(layouts_btn)
        self.layout.addWidget(signal_and_slot_btn)
        self.layout.addWidget(todo_btn)
        self.layout.addWidget(gallery_btn)

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

    def open_signal_and_slot(self):
        if self.signal_and_slot is None:
            self.signal_and_slot = SignalAndSlot(self)
        self.signal_and_slot.show()
        self.hide()

    def open_todoapp(self):
        if self.todoapp is None:
            self.todoapp = Todo(self)
        self.todoapp.show()
        self.hide()

    def open_widget_gallery(self):
        if self.widget_gallery is None:
            self.widget_gallery = WidgetGallery(self)
        self.widget_gallery.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("""
    QPushButton:hover {
    background-color: green; 
    color: #8888ff;
    }
    """)  # 没有解决背景色的问题
    window.show()
    sys.exit(app.exec())

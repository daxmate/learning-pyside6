from PySide6.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QPushButton, QWidget, QHBoxLayout, QGridLayout
import sys


class Layouts(QMainWindow):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.temp_widget = None
        self.mainwindow = mainwindow
        self.buttons = [QPushButton(text) for text in ["垂直布局", "水平布局", "栅格布局", "按钮1", "按钮2"]]
        self.last_layout = None
        self.init_ui()

    def init_ui(self):
        """初始化UI"""

        # 设置窗口大小并移动窗口到屏幕中央
        self.resize(600, 300)
        self.setWindowTitle("Layouts各种窗口布局")
        screen_center = self.screen().availableGeometry().center()
        self.geometry().moveCenter(screen_center)

        # 初始化为垂直布局，并将按钮添加到布局中
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
        for button in self.buttons:
            layout.addWidget(button)
        self.setCentralWidget(central_widget)

        # 记录最后的布局
        self.last_layout = layout

        # 链接点击信号到相应的切换布局函数
        self.buttons[0].clicked.connect(lambda: self.switch_layout(QVBoxLayout()))
        self.buttons[1].clicked.connect(lambda: self.switch_layout(QHBoxLayout()))
        self.buttons[2].clicked.connect(lambda: self.switch_layout(QGridLayout()))

    def switch_layout(self, layout):
        """切换UI布局"""

        # 如果布局与最后的布局一样则直接返回
        if isinstance(layout, type(self.last_layout)):
            return

        # 记录最后的布局为新的布局
        self.last_layout = layout

        # 将原来的布局存储为旧布局
        old_layout = self.centralWidget().layout()

        # 新建一个临时窗体控件，并将旧布局链接到临时控件上，同时将新布局设置到中央控件上
        self.temp_widget = QWidget()
        if old_layout:
            self.temp_widget.setLayout(old_layout)
        self.centralWidget().setLayout(layout)
        # 从旧布局上移动按钮到新布局上
        if not isinstance(layout, QGridLayout):
            for button in self.buttons:
                layout.addWidget(button)
        else:
            for index, button in enumerate(self.buttons):
                layout.addWidget(button, index // 2, index % 2)

    def closeEvent(self, event):
        """关闭本窗口时显示主窗口"""
        if self.mainwindow and not self.mainwindow.isVisible():
            self.mainwindow.show()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Layouts()
    window.show()
    sys.exit(app.exec())

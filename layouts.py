from PyQt6.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QPushButton, QWidget, QHBoxLayout, QGridLayout
import sys


class Layouts(QMainWindow):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.temp_widget = None
        self.mainwindow = mainwindow
        self.buttons = [QPushButton(text) for text in ["垂直布局", "水平布局", "栅格布局", "按钮1", "按钮2"]]
        self.resize(600, 300)
        self.setWindowTitle("Layouts各种窗口布局")
        self.layouts()
        self.center()

    def center(self):
        screen_center = self.screen().availableGeometry().center()
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(screen_center)

    def layouts(self):
        vl = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(vl)
        self.buttons[0].clicked.connect(self.vertical_layout)
        self.buttons[1].clicked.connect(self.horizontal_layout)
        self.buttons[2].clicked.connect(self.grid_layout)
        for button in self.buttons:
            vl.addWidget(button)
        self.setCentralWidget(central_widget)

    def vertical_layout(self):
        self.remove_layout()

        vl = QVBoxLayout()
        for button in self.buttons:
            vl.addWidget(button)
        self.centralWidget().setLayout(vl)

    def horizontal_layout(self):
        self.remove_layout()

        hl = QHBoxLayout()
        for button in self.buttons:
            hl.addWidget(button)
        self.centralWidget().setLayout(hl)

    def grid_layout(self):
        self.remove_layout()

        gl = QGridLayout()
        for index, button in enumerate(self.buttons):
            gl.addWidget(button, index // 2, index % 2)
        self.centralWidget().setLayout(gl)

    def remove_layout(self):
        central_widget = self.centralWidget()
        old_layout = central_widget.layout()

        self.temp_widget = QWidget()
        self.temp_widget.setLayout(old_layout)

    def closeEvent(self, event):
        if self.mainwindow and not self.mainwindow.isVisible():
            self.mainwindow.show()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Layouts()
    window.show()
    sys.exit(app.exec())

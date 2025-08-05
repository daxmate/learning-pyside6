from PySide6.QtWidgets import (QWidget,
                               QVBoxLayout,
                               QPushButton,
                               QHBoxLayout,
                               QGridLayout,
                               QFormLayout,
                               QLineEdit,
                               QSpinBox,
                               QComboBox,
                               QCheckBox,
                               QApplication, QSizePolicy,
                               )
from PySide6.QtGui import (
    QPixmap, Qt
)

import qlementine_icons_16_software_rc

from layout import Ui_LayoutWindow
import sys


class Layouts(QWidget, Ui_LayoutWindow):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.setupUi(self)
        self.buttons = self.get_buttons()

        self.vertical_btn.clicked.connect(lambda: self.switch_layout(layout=QVBoxLayout()))
        self.horizontal_btn.clicked.connect(lambda: self.switch_layout(layout=QHBoxLayout()))
        self.grid_btn.clicked.connect(lambda: self.switch_layout(layout=QGridLayout()))
        self.form_btn.clicked.connect(lambda: self.switch_layout(layout=QFormLayout()))

    def get_buttons(self):
        buttons = []
        layout = self.display_widget.layout()
        for index in range(layout.count()):
            item = layout.itemAt(index)
            if item:
                widget = item.widget()
                if isinstance(widget, QPushButton):
                    buttons.append(widget)
        return buttons

    def switch_layout(self, layout):
        old_layout = self.display_widget.layout()
        if type(old_layout) == type(layout):
            return
        temp_widget = QWidget(self)
        if old_layout:
            temp_widget.setLayout(old_layout)
        self.display_widget.setLayout(layout)
        if not isinstance(layout, QGridLayout) and not isinstance(layout, QFormLayout):
            for button in self.buttons:
                layout.addWidget(button)
        elif isinstance(layout, QGridLayout):
            self.grid_layout()
        elif isinstance(layout, QFormLayout):
            self.form_layout()

    def grid_layout(self):
        button_texts = ["AC"]
        button_texts.extend(list("±%÷789x456-123+⊕0.="))

        layout = self.display_widget.layout()
        buttons = []
        for index, text in enumerate(button_texts):
            button = QPushButton(text)
            buttons.append(button)
            sp = button.sizePolicy()
            sp.setVerticalPolicy(QSizePolicy.Policy.Minimum)
            button.setSizePolicy(sp)
            font = button.font()
            font.setPointSize(32)
            button.setFont(font)
            layout.addWidget(buttons[index], index // 4, index % 4)

    def form_layout(self):
        form_layout = self.display_widget.layout()
        form_layout.addRow("用户名:", QLineEdit())
        form_layout.addRow("密码:", QLineEdit(echoMode=QLineEdit.EchoMode.Password))
        spin = QSpinBox()
        spin.setValue(45)
        form_layout.addRow("年龄:", spin)
        combo = QComboBox()
        combo.addItems(["男", "女"])
        combo.setCurrentIndex(1)
        form_layout.addRow("性别:", combo)
        form_layout.addRow(QCheckBox("记住登录信息"))

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

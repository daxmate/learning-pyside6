from PySide6.QtWidgets import QWidget, QToolButton

from widget_gallery_ui import Ui_Form
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu


class WidgetGallery(QWidget, Ui_Form):
    def __init__(self, mainwindow=None):
        super().__init__()
        self.mainwindow = mainwindow
        self.setupUi(self)


        tool_menu = QMenu(self.option_tool_button)
        tool_menu.addAction("Option")
        tool_menu.addSeparator()
        tool_menu.addAction("Exit")
        self.option_tool_button.setMenu(tool_menu)

    def closeEvent(self, event):
        if self.mainwindow is not None and self.isVisible():
            self.hide()
            self.mainwindow.show()

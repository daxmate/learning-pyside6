from PySide6.QtCore import QDir
from PySide6.QtWidgets import QStyleFactory, QTabWidget, QFileSystemModel
from PySide6.QtWidgets import QWidget, QApplication

from resources.forms.widget_gallery import Ui_Form
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

        self.add_style()
        self.setup_tab_widget()

    def add_style(self):
        """
        将默认系统样式排在首位并添加到组合框
        :return:
        """
        default_style_name = QApplication.style().objectName().lower()

        style_names = []
        for style_name in QStyleFactory.keys():
            if style_name.lower() == default_style_name:
                style_names.insert(0, style_name)
            else:
                style_names.append(style_name)

        self.style_comb.addItems(style_names)

        self.style_comb.currentIndexChanged.connect(self.switch_style)

    def switch_style(self):
        current_style = self.style_comb.currentText()
        QApplication.setStyle(current_style)

    def setup_tab_widget(self):
        filesystem_model = QFileSystemModel()
        filesystem_model.setRootPath(QDir.rootPath())

        self.treeView.setModel(filesystem_model)

    def closeEvent(self, event):
        if self.mainwindow is not None and self.isVisible():
            self.hide()
            self.mainwindow.show()

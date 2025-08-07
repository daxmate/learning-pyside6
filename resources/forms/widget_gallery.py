# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_gallery.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QCheckBox,
    QComboBox, QCommandLinkButton, QDateTimeEdit, QDial,
    QDialogButtonBox, QFontComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QKeySequenceEdit, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QScrollBar, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)

from filesystem_treeview import FileSystemTreeView
import qlementine_icons_16_navigation_rc
import qlementine_icons_16_shopping_rc
import qlementine_icons_16_software_rc
import qlementine_icons_16_text_rc
import qlementine_icons_16_action_rc
import qlementine_icons_16_audio_rc
import qlementine_icons_16_brand_rc
import qlementine_icons_16_document_rc
import qlementine_icons_16_file_rc
import qlementine_icons_16_food_rc
import qlementine_icons_16_hardware_rc
import qlementine_icons_16_instrument_rc
import qlementine_icons_16_media_rc
import qlementine_icons_16_misc_rc
import qlementine_icons_16_page_rc
import qlementine_icons_16_shape_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(802, 906)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 135, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.style_label = QLabel(self.layoutWidget)
        self.style_label.setObjectName(u"style_label")

        self.horizontalLayout_3.addWidget(self.style_label)

        self.style_comb = QComboBox(self.layoutWidget)
        self.style_comb.setObjectName(u"style_comb")

        self.horizontalLayout_3.addWidget(self.style_comb)

        self.tab_widget = QTabWidget(Form)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_widget.setGeometry(QRect(10, 340, 471, 521))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.treeView = FileSystemTreeView(self.tab)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_3.addWidget(self.treeView)

        self.toggle_hidden_cb = QCheckBox(self.tab)
        self.toggle_hidden_cb.setObjectName(u"toggle_hidden_cb")

        self.verticalLayout_3.addWidget(self.toggle_hidden_cb)

        self.tab_widget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.listWidget = QListWidget(self.tab_2)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_6.addWidget(self.listWidget)

        self.tab_widget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listView = QListView(self.tab_3)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout_4.addWidget(self.listView)

        self.tab_widget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.listView_2 = QListView(self.tab_4)
        self.listView_2.setObjectName(u"listView_2")

        self.horizontalLayout_7.addWidget(self.listView_2)

        self.tab_widget.addTab(self.tab_4, "")
        self.buttons_gb = QGroupBox(Form)
        self.buttons_gb.setObjectName(u"buttons_gb")
        self.buttons_gb.setGeometry(QRect(11, 40, 272, 281))
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_gb)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.buttons_gb)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/software/character-map.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.buttons_gb)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/action/on-off.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.buttons_gb)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/action/flatten.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton = QToolButton(self.buttons_gb)
        self.toolButton.setObjectName(u"toolButton")
        icon3 = QIcon()
        icon3.addFile(u":/navigation/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.toolButton)

        self.option_tool_button = QToolButton(self.buttons_gb)
        self.option_tool_button.setObjectName(u"option_tool_button")
        icon4 = QIcon()
        icon4.addFile(u":/navigation/menu-burger.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.option_tool_button.setIcon(icon4)
        self.option_tool_button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

        self.horizontalLayout.addWidget(self.option_tool_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.commandLinkButton = QCommandLinkButton(self.buttons_gb)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.BatteryLow))
        self.commandLinkButton.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.commandLinkButton)

        self.buttonBox = QDialogButtonBox(self.buttons_gb)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton_2 = QRadioButton(self.buttons_gb)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.buttons_gb)
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.buttons_gb)
        self.buttonGroup.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.checkBox_4 = QCheckBox(self.buttons_gb)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setTristate(True)

        self.verticalLayout.addWidget(self.checkBox_4)

        self.checkBox = QCheckBox(self.buttons_gb)
        self.buttonGroup_2 = QButtonGroup(Form)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.setExclusive(False)
        self.buttonGroup_2.addButton(self.checkBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(False)

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.buttons_gb)
        self.buttonGroup_2.addButton(self.checkBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setTristate(False)

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.buttons_gb)
        self.buttonGroup_2.addButton(self.checkBox_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setTristate(False)

        self.verticalLayout.addWidget(self.checkBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.input_gb = QGroupBox(Form)
        self.input_gb.setObjectName(u"input_gb")
        self.input_gb.setGeometry(QRect(299, 47, 271, 274))
        self.input_gb.setCheckable(True)
        self.gridLayout = QGridLayout(self.input_gb)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit = QLineEdit(self.input_gb)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.verticalScrollBar = QScrollBar(self.input_gb)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setValue(50)
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout.addWidget(self.verticalScrollBar, 0, 1, 3, 1)

        self.verticalSlider = QSlider(self.input_gb)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setValue(50)
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.spinBox = QSpinBox(self.input_gb)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(50)

        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.input_gb)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setDate(QDate(2025, 8, 6))
        self.dateTimeEdit.setTime(QTime(12, 0, 0))

        self.gridLayout.addWidget(self.dateTimeEdit, 2, 0, 1, 1)

        self.horizontalScrollBar = QScrollBar(self.input_gb)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        self.horizontalScrollBar.setValue(50)
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.horizontalScrollBar, 3, 0, 1, 1)

        self.keySequenceEdit = QKeySequenceEdit(self.input_gb)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")

        self.gridLayout.addWidget(self.keySequenceEdit, 3, 1, 1, 2)

        self.horizontalSlider = QSlider(self.input_gb)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 4, 0, 1, 1)

        self.dial = QDial(self.input_gb)
        self.dial.setObjectName(u"dial")
        self.dial.setValue(50)

        self.gridLayout.addWidget(self.dial, 4, 1, 2, 1)

        self.fontComboBox = QFontComboBox(self.input_gb)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.gridLayout.addWidget(self.fontComboBox, 5, 0, 1, 1)


        self.retranslateUi(Form)

        self.tab_widget.setCurrentIndex(1)
        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5e38\u7528\u63a7\u4ef6", None))
        self.style_label.setText(QCoreApplication.translate("Form", u"\u6837\u5f0f", None))
        self.toggle_hidden_cb.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u9690\u85cf\u6587\u4ef6", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab), QCoreApplication.translate("Form", u"Tree View", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Table", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"List", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Icon Mode List", None))
        self.buttons_gb.setTitle(QCoreApplication.translate("Form", u"\u6309\u94ae", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u9ed8\u8ba4\u6309\u94ae", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5207\u6362\u6309\u94ae", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5e73\u9762\u6309\u94ae", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"\u5de5\u5177\u6309\u94ae", None))
        self.option_tool_button.setText(QCoreApplication.translate("Form", u"\u83dc\u5355\u6309\u94ae", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Form", u"\u5173\u673a", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("Form", u"\u7535\u91cf\u4f4e\uff0c\u70b9\u51fb\u5173\u673a\uff01", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u5355\u9009\u6309\u94ae1", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u5355\u9009\u6309\u94ae2", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u5355\u9009\u6309\u94ae3", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u4e09\u6001\u9009\u62e9\u6846", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u591a\u9009\u68461", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u591a\u9009\u68462", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u591a\u9009\u68463", None))
        self.input_gb.setTitle(QCoreApplication.translate("Form", u"\u7b80\u5355\u8f93\u5165\u63a7\u4ef6", None))
    # retranslateUi


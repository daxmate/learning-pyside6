# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListView,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_view = QListView(Form)
        self.list_view.setObjectName(u"list_view")

        self.verticalLayout.addWidget(self.list_view)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delete_btn = QPushButton(Form)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout.addWidget(self.delete_btn)

        self.complete_btn = QPushButton(Form)
        self.complete_btn.setObjectName(u"complete_btn")

        self.horizontalLayout.addWidget(self.complete_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_edit = QLineEdit(Form)
        self.line_edit.setObjectName(u"line_edit")

        self.verticalLayout.addWidget(self.line_edit)

        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"add_btn")

        self.verticalLayout.addWidget(self.add_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Todo List", None))
        self.delete_btn.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.complete_btn.setText(QCoreApplication.translate("Form", u"Complete", None))
        self.add_btn.setText(QCoreApplication.translate("Form", u"Add", None))
    # retranslateUi


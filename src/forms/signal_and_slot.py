# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signal_and_slot.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(400, 300)
        self.gridLayout = QGridLayout(widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.up_btn = QPushButton(widget)
        self.up_btn.setObjectName(u"up_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up_btn.sizePolicy().hasHeightForWidth())
        self.up_btn.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.up_btn.setIcon(icon)
        self.up_btn.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.up_btn, 0, 1, 1, 1)

        self.left_btn = QPushButton(widget)
        self.left_btn.setObjectName(u"left_btn")
        sizePolicy.setHeightForWidth(self.left_btn.sizePolicy().hasHeightForWidth())
        self.left_btn.setSizePolicy(sizePolicy)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.left_btn.setIcon(icon1)
        self.left_btn.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.left_btn, 1, 0, 1, 1)

        self.right_btn = QPushButton(widget)
        self.right_btn.setObjectName(u"right_btn")
        sizePolicy.setHeightForWidth(self.right_btn.sizePolicy().hasHeightForWidth())
        self.right_btn.setSizePolicy(sizePolicy)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.right_btn.setIcon(icon2)
        self.right_btn.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.right_btn, 1, 2, 1, 1)

        self.down_btn = QPushButton(widget)
        self.down_btn.setObjectName(u"down_btn")
        sizePolicy.setHeightForWidth(self.down_btn.sizePolicy().hasHeightForWidth())
        self.down_btn.setSizePolicy(sizePolicy)
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.down_btn.setIcon(icon3)
        self.down_btn.setIconSize(QSize(48, 48))

        self.gridLayout.addWidget(self.down_btn, 2, 1, 1, 1)


        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"\u79fb\u52a8\u7684\u7a97\u53e3", None))
        self.up_btn.setText("")
        self.left_btn.setText("")
        self.right_btn.setText("")
        self.down_btn.setText("")
    # retranslateUi


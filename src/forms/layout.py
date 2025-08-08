# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LayoutWindow(object):
    def setupUi(self, LayoutWindow):
        if not LayoutWindow.objectName():
            LayoutWindow.setObjectName(u"LayoutWindow")
        LayoutWindow.resize(600, 500)
        self.verticalLayout = QVBoxLayout(LayoutWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontal_btn = QPushButton(LayoutWindow)
        self.horizontal_btn.setObjectName(u"horizontal_btn")

        self.horizontalLayout_2.addWidget(self.horizontal_btn)

        self.vertical_btn = QPushButton(LayoutWindow)
        self.vertical_btn.setObjectName(u"vertical_btn")

        self.horizontalLayout_2.addWidget(self.vertical_btn)

        self.form_btn = QPushButton(LayoutWindow)
        self.form_btn.setObjectName(u"form_btn")

        self.horizontalLayout_2.addWidget(self.form_btn)

        self.grid_btn = QPushButton(LayoutWindow)
        self.grid_btn.setObjectName(u"grid_btn")

        self.horizontalLayout_2.addWidget(self.grid_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.display_widget = QWidget(LayoutWindow)
        self.display_widget.setObjectName(u"display_widget")
        self.horizontalLayout = QHBoxLayout(self.display_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_5 = QPushButton(self.display_widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(48)
        self.pushButton_5.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_8 = QPushButton(self.display_widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.display_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.display_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.display_widget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_9)


        self.verticalLayout.addWidget(self.display_widget)


        self.retranslateUi(LayoutWindow)

        QMetaObject.connectSlotsByName(LayoutWindow)
    # setupUi

    def retranslateUi(self, LayoutWindow):
        LayoutWindow.setWindowTitle(QCoreApplication.translate("LayoutWindow", u"\u56db\u79cd\u5e03\u5c40", None))
        self.horizontal_btn.setText(QCoreApplication.translate("LayoutWindow", u"\u6a2a\u5411\u5e03\u5c40", None))
        self.vertical_btn.setText(QCoreApplication.translate("LayoutWindow", u"\u7eb5\u5411\u5e03\u5c40", None))
        self.form_btn.setText(QCoreApplication.translate("LayoutWindow", u"\u8868\u5355\u5e03\u5c40", None))
        self.grid_btn.setText(QCoreApplication.translate("LayoutWindow", u"\u7f51\u683c\u5e03\u5c40", None))
        self.pushButton_5.setText(QCoreApplication.translate("LayoutWindow", u"\u25c9", None))
        self.pushButton_8.setText(QCoreApplication.translate("LayoutWindow", u"\u25c9", None))
        self.pushButton_6.setText(QCoreApplication.translate("LayoutWindow", u"\u25c9", None))
        self.pushButton_7.setText(QCoreApplication.translate("LayoutWindow", u"\u25c9", None))
        self.pushButton_9.setText(QCoreApplication.translate("LayoutWindow", u"\u25c9", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guess_number.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_guess(object):
    def setupUi(self, guess):
        if not guess.objectName():
            guess.setObjectName(u"guess")
        guess.resize(400, 300)
        self.gridLayout = QGridLayout(guess)
        self.gridLayout.setObjectName(u"gridLayout")
        self.input_sb = QSpinBox(guess)
        self.input_sb.setObjectName(u"input_sb")
        self.input_sb.setMinimum(1)
        self.input_sb.setMaximum(100)
        self.input_sb.setValue(50)

        self.gridLayout.addWidget(self.input_sb, 1, 0, 1, 1)

        self.result_label = QLabel(guess)
        self.result_label.setObjectName(u"result_label")
        font = QFont()
        font.setPointSize(32)
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.result_label, 2, 0, 1, 2)

        self.confirm_btn = QPushButton(guess)
        self.confirm_btn.setObjectName(u"confirm_btn")

        self.gridLayout.addWidget(self.confirm_btn, 1, 1, 1, 1)

        self.question_label = QLabel(guess)
        self.question_label.setObjectName(u"question_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.question_label.sizePolicy().hasHeightForWidth())
        self.question_label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(18)
        self.question_label.setFont(font1)
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.question_label, 0, 0, 1, 2)

        self.restart_btn = QPushButton(guess)
        self.restart_btn.setObjectName(u"restart_btn")

        self.gridLayout.addWidget(self.restart_btn, 3, 0, 1, 2)


        self.retranslateUi(guess)

        QMetaObject.connectSlotsByName(guess)
    # setupUi

    def retranslateUi(self, guess):
        guess.setWindowTitle(QCoreApplication.translate("guess", u"\u731c\u6570\u5b57", None))
        self.result_label.setText("")
        self.confirm_btn.setText(QCoreApplication.translate("guess", u"\u786e\u8ba4\u8f93\u5165", None))
        self.question_label.setText(QCoreApplication.translate("guess", u"\u6211\u6709\u4e00\u4e2a1\u5230100\u7684\u6574\u6570\uff0c\u8bf7\u731c\u731c\u662f\u591a\u5c11\uff1f", None))
        self.restart_btn.setText(QCoreApplication.translate("guess", u"\u518d\u6765\u4e00\u5c40", None))
    # retranslateUi


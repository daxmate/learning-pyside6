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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import qlementine_icons_16_hardware_rc
import qlementine_icons_16_action_rc
import qlementine_icons_16_navigation_rc

class Ui_guess(object):
    def setupUi(self, guess):
        if not guess.objectName():
            guess.setObjectName(u"guess")
        guess.resize(615, 410)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(guess.sizePolicy().hasHeightForWidth())
        guess.setSizePolicy(sizePolicy)
        guess.setStyleSheet(u"QPushButton[objectName^=num]{\n"
"color: rgb(124, 126, 126);\n"
"}\n"
"\n"
"#confirm_btn{\n"
"color: rgb(255, 195, 161);\n"
"}\n"
"\n"
"#delete_btn{\n"
"color: rgb(255, 88, 122);\n"
"}\n"
"\n"
"#guess_le{\n"
"color: rgb(57, 127, 255);\n"
"font-size: 48px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(guess)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.question_label = QLabel(guess)
        self.question_label.setObjectName(u"question_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.question_label.sizePolicy().hasHeightForWidth())
        self.question_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(32)
        self.question_label.setFont(font)
        self.question_label.setStyleSheet(u"#question_label{\n"
"color:rgb(0, 123, 167)\n"
"}")
        self.question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.question_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.guess_le = QLineEdit(guess)
        self.guess_le.setObjectName(u"guess_le")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.guess_le.sizePolicy().hasHeightForWidth())
        self.guess_le.setSizePolicy(sizePolicy2)
        font1 = QFont()
        self.guess_le.setFont(font1)
        self.guess_le.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.guess_le)

        self.result_label = QLabel(guess)
        self.result_label.setObjectName(u"result_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.result_label.sizePolicy().hasHeightForWidth())
        self.result_label.setSizePolicy(sizePolicy3)
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.result_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.num8_btn = QPushButton(guess)
        self.num8_btn.setObjectName(u"num8_btn")
        sizePolicy2.setHeightForWidth(self.num8_btn.sizePolicy().hasHeightForWidth())
        self.num8_btn.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"JetBrainsMonoNL Nerd Font Mono"])
        font2.setPointSize(32)
        font2.setBold(True)
        self.num8_btn.setFont(font2)

        self.gridLayout.addWidget(self.num8_btn, 3, 1, 1, 1)

        self.num5_btn = QPushButton(guess)
        self.num5_btn.setObjectName(u"num5_btn")
        sizePolicy2.setHeightForWidth(self.num5_btn.sizePolicy().hasHeightForWidth())
        self.num5_btn.setSizePolicy(sizePolicy2)
        self.num5_btn.setFont(font2)

        self.gridLayout.addWidget(self.num5_btn, 1, 1, 1, 1)

        self.num0_btn = QPushButton(guess)
        self.num0_btn.setObjectName(u"num0_btn")
        sizePolicy2.setHeightForWidth(self.num0_btn.sizePolicy().hasHeightForWidth())
        self.num0_btn.setSizePolicy(sizePolicy2)
        self.num0_btn.setFont(font2)
        self.num0_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.num0_btn, 4, 0, 1, 1)

        self.num4_btn = QPushButton(guess)
        self.num4_btn.setObjectName(u"num4_btn")
        sizePolicy2.setHeightForWidth(self.num4_btn.sizePolicy().hasHeightForWidth())
        self.num4_btn.setSizePolicy(sizePolicy2)
        self.num4_btn.setFont(font2)

        self.gridLayout.addWidget(self.num4_btn, 1, 0, 1, 1)

        self.num3_btn = QPushButton(guess)
        self.num3_btn.setObjectName(u"num3_btn")
        sizePolicy2.setHeightForWidth(self.num3_btn.sizePolicy().hasHeightForWidth())
        self.num3_btn.setSizePolicy(sizePolicy2)
        self.num3_btn.setFont(font2)

        self.gridLayout.addWidget(self.num3_btn, 0, 2, 1, 1)

        self.num7_btn = QPushButton(guess)
        self.num7_btn.setObjectName(u"num7_btn")
        sizePolicy2.setHeightForWidth(self.num7_btn.sizePolicy().hasHeightForWidth())
        self.num7_btn.setSizePolicy(sizePolicy2)
        self.num7_btn.setFont(font2)

        self.gridLayout.addWidget(self.num7_btn, 3, 0, 1, 1)

        self.num1_btn = QPushButton(guess)
        self.num1_btn.setObjectName(u"num1_btn")
        sizePolicy2.setHeightForWidth(self.num1_btn.sizePolicy().hasHeightForWidth())
        self.num1_btn.setSizePolicy(sizePolicy2)
        self.num1_btn.setFont(font2)

        self.gridLayout.addWidget(self.num1_btn, 0, 0, 1, 1)

        self.num2_btn = QPushButton(guess)
        self.num2_btn.setObjectName(u"num2_btn")
        sizePolicy2.setHeightForWidth(self.num2_btn.sizePolicy().hasHeightForWidth())
        self.num2_btn.setSizePolicy(sizePolicy2)
        self.num2_btn.setFont(font2)

        self.gridLayout.addWidget(self.num2_btn, 0, 1, 1, 1)

        self.num6_btn = QPushButton(guess)
        self.num6_btn.setObjectName(u"num6_btn")
        sizePolicy2.setHeightForWidth(self.num6_btn.sizePolicy().hasHeightForWidth())
        self.num6_btn.setSizePolicy(sizePolicy2)
        self.num6_btn.setFont(font2)

        self.gridLayout.addWidget(self.num6_btn, 1, 2, 1, 1)

        self.num9_btn = QPushButton(guess)
        self.num9_btn.setObjectName(u"num9_btn")
        sizePolicy2.setHeightForWidth(self.num9_btn.sizePolicy().hasHeightForWidth())
        self.num9_btn.setSizePolicy(sizePolicy2)
        self.num9_btn.setFont(font2)

        self.gridLayout.addWidget(self.num9_btn, 3, 2, 1, 1)

        self.confirm_btn = QPushButton(guess)
        self.confirm_btn.setObjectName(u"confirm_btn")
        sizePolicy2.setHeightForWidth(self.confirm_btn.sizePolicy().hasHeightForWidth())
        self.confirm_btn.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"JetBrainsMonoNL Nerd Font Mono"])
        font3.setPointSize(8)
        font3.setBold(True)
        self.confirm_btn.setFont(font3)
        icon = QIcon()
        icon.addFile(u":/navigation/key-return-noframe.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.confirm_btn.setIcon(icon)

        self.gridLayout.addWidget(self.confirm_btn, 4, 1, 1, 1)

        self.delete_btn = QPushButton(guess)
        self.delete_btn.setObjectName(u"delete_btn")
        sizePolicy2.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy2)
        self.delete_btn.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u":/action/erase.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.delete_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.delete_btn, 4, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.restart_btn = QPushButton(guess)
        self.restart_btn.setObjectName(u"restart_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.restart_btn.sizePolicy().hasHeightForWidth())
        self.restart_btn.setSizePolicy(sizePolicy4)
        self.restart_btn.setFont(font)
        self.restart_btn.setStyleSheet(u"#restart_btn{\n"
"color: rgb(0, 123, 167)\n"
"}")

        self.verticalLayout_2.addWidget(self.restart_btn)


        self.retranslateUi(guess)

        QMetaObject.connectSlotsByName(guess)
    # setupUi

    def retranslateUi(self, guess):
        guess.setWindowTitle(QCoreApplication.translate("guess", u"\u731c\u6570\u5b57", None))
        self.question_label.setText(QCoreApplication.translate("guess", u"\u6211\u6709\u4e00\u4e2a1\u5230100\u7684\u6574\u6570\uff0c\n"
"\u8bf7\u731c\u731c\u662f\u591a\u5c11\uff1f", None))
        self.guess_le.setText(QCoreApplication.translate("guess", u"50", None))
        self.result_label.setText("")
        self.num8_btn.setText(QCoreApplication.translate("guess", u"8", None))
        self.num5_btn.setText(QCoreApplication.translate("guess", u"5", None))
        self.num0_btn.setText(QCoreApplication.translate("guess", u"0", None))
        self.num4_btn.setText(QCoreApplication.translate("guess", u"4", None))
        self.num3_btn.setText(QCoreApplication.translate("guess", u"3", None))
        self.num7_btn.setText(QCoreApplication.translate("guess", u"7", None))
        self.num1_btn.setText(QCoreApplication.translate("guess", u"1", None))
        self.num2_btn.setText(QCoreApplication.translate("guess", u"2", None))
        self.num6_btn.setText(QCoreApplication.translate("guess", u"6", None))
        self.num9_btn.setText(QCoreApplication.translate("guess", u"9", None))
        self.confirm_btn.setText("")
        self.delete_btn.setText("")
        self.restart_btn.setText(QCoreApplication.translate("guess", u"\u518d\u6765\u4e00\u5c40", None))
    # retranslateUi


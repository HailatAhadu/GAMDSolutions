# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TIN_Checker.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TIN_Checker(object):
    def setupUi(self, TIN_Checker):
        if not TIN_Checker.objectName():
            TIN_Checker.setObjectName(u"TIN_Checker")
        TIN_Checker.resize(720, 590)
        TIN_Checker.setMinimumSize(QSize(720, 590))
        TIN_Checker.setMaximumSize(QSize(720, 590))
        self.centralwidget = QWidget(TIN_Checker)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(226, 237, 254);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setFrameShape(QFrame.NoFrame)
        self.mainframe.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.mainframe)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.mainframe)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(700, 50))
        self.header.setMaximumSize(QSize(700, 50))
        self.header.setStyleSheet(u"backgroung-color: rgb(226, 237, 254);")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-family:Arial Black;\n"
"font-size: 40px;")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.closebtn = QPushButton(self.header)
        self.closebtn.setObjectName(u"closebtn")
        self.closebtn.setMinimumSize(QSize(45, 45))
        self.closebtn.setMaximumSize(QSize(45, 45))
        self.closebtn.setStyleSheet(u"font-weight:bold;\n"
"")

        self.horizontalLayout_2.addWidget(self.closebtn)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignVCenter)

        self.body = QFrame(self.mainframe)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(0, 450))
        self.body.setFrameShape(QFrame.NoFrame)
        self.body.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.textinput = QLineEdit(self.frame)
        self.textinput.setObjectName(u"textinput")
        self.textinput.setMinimumSize(QSize(0, 40))
        self.textinput.setMaximumSize(QSize(16777215, 40))
        self.textinput.setStyleSheet(u"font-family: Times New Roman;\n"
"font-size: 20px;\n"
"text-align: center;\n"
"background-color:rgb(255,255,255);")

        self.horizontalLayout_4.addWidget(self.textinput)

        self.searchbtn = QPushButton(self.frame)
        self.searchbtn.setObjectName(u"searchbtn")
        self.searchbtn.setMinimumSize(QSize(100, 40))
        self.searchbtn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_4.addWidget(self.searchbtn)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.body)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 350))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tag = QPlainTextEdit(self.frame_2)
        self.tag.setObjectName(u"tag")
        self.tag.setMinimumSize(QSize(150, 0))
        self.tag.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_5.addWidget(self.tag)

        self.text = QPlainTextEdit(self.frame_2)
        self.text.setObjectName(u"text")

        self.horizontalLayout_5.addWidget(self.text)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.body)

        self.footer = QFrame(self.mainframe)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(700, 30))
        self.footer.setMaximumSize(QSize(700, 30))
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.mainframe)

        TIN_Checker.setCentralWidget(self.centralwidget)

        self.retranslateUi(TIN_Checker)

        QMetaObject.connectSlotsByName(TIN_Checker)
    # setupUi

    def retranslateUi(self, TIN_Checker):
        TIN_Checker.setWindowTitle(QCoreApplication.translate("TIN_Checker", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("TIN_Checker", u"TIN Checker", None))
        self.closebtn.setText(QCoreApplication.translate("TIN_Checker", u"X", None))
        self.textinput.setText("")
        self.textinput.setPlaceholderText(QCoreApplication.translate("TIN_Checker", u"Seach for TIN number", None))
        self.searchbtn.setText(QCoreApplication.translate("TIN_Checker", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("TIN_Checker", u"Developed by: GAMD Solutions", None))
    # retranslateUi


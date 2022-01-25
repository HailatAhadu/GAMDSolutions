import sys
import platform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
import xml.etree.ElementTree
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

from TINChecker import Ui_MainWindow
        
url = "http://www.erca.gov.et:8008/wserca/index.jsf?tin="
class TINChecker(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton.clicked.connect(lambda: self.clickMe())
       
        self.show()

    def clickMe(self):
        tin = self.ui.lineEdit.text()
        if not tin:
            self.ui.text.setPlainText("Input Error \n Please input the Tin Number and try again")
            self.ui.tag.setPlainText("")
        elif not tin.isdigit():
            self.ui.text.setPlainText("Input Error \n Please input number not other character")
            self.ui.tag.setPlainText("")
        else:
            try:
                # request = requests.get(url + tin, timeout=timeout)
                req = requests.get(url + tin).text
                data1 = BeautifulSoup(req, 'lxml')
                body = data1.body.text
                body = body.strip()

                try:
                    myroot = ET.fromstring(body)
                    mytree = list(myroot)
                    z = 0
                    tag = ""
                    text = ""

                    for y in mytree:
                        tag += y.tag + "\n"
                        text += y.text +"\n"
                        z = z + 1
                    self.ui.tag.setPlainText(tag)
                    self.ui.text.setPlainText(text)

                except xml.etree.ElementTree.ParseError as err:
                    self.ui.text.setPlainText("Input Error \n The TIN Number you input is not find")
                    self.ui.tag.setPlainText("")

            except (requests.ConnectionError, requests.Timeout):
                self.ui.text.setPlainText("Input Error \n Please check the Internet Connection")
                self.ui.tag.setPlainText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TINChecker()
    sys.exit(app.exec())

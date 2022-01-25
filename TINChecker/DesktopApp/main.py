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

from TIN_Checker import Ui_TIN_Checker
        
url = "http://www.erca.gov.et:8008/wserca/index.jsf?tin="

class TINChecker(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_TIN_Checker()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.closebtn.clicked.connect(lambda: self.close())
        self.ui.searchbtn.clicked.connect(lambda: self.clickMe())
       
        self.show()
    
    def clickMe(self):
        tin = self.ui.textinput.text()
        # self.ui.textoutput.setPlainText(tin)
        if not tin:
            self.ui.textoutput.setPlainText("Input Error", "Please input the Tin Number and try again")
        elif not tin.isdigit():
            self.ui.textoutput.setPlainText("Input Error", "Please input number not other character")
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
                    self.ui.textoutput.setPlainText("Input Error", "The TIN Number you input is not find")

            except (requests.ConnectionError, requests.Timeout):
                self.ui.textoutput.setPlainText("Input Error", "Please check the Internet Connection")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TINChecker()
    sys.exit(app.exec())

# -*- coding:UTF-8 -*-
'''
加载显示外部的web页面
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.setWindowTitle("打开外部网页例子")
        self.setGeometry(5,30,1355,730)

        self.browser=QWebEngineView()
        #加载外部的Web页面
        self.browser.load(QUrl('http://www.cnblogs.com/wangshuo1'))
        self.setCentralWidget(self.browser)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())



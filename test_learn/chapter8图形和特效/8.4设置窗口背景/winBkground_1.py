# -*- coding:UTF-8 -*-
'''
使用QSS设置窗口背景
setPixmap或者setIcon设置背景图片或者图标
'''
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)
win=QMainWindow()
win.setWindowTitle("界面背景图片设置")
win.resize(350,  250)
#设置窗口名
win.setObjectName("MainWindow")
#设置图片的相对路径
win.setStyleSheet("#MainWindow{border-image:url(../img/python.jpg);}")

win.show()

sys.exit(app.exec_())

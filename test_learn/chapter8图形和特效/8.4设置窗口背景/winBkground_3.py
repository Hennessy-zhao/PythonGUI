# -*- coding:UTF-8 -*-
'''
使用QPalette设置窗口背景
使用QPalette调色盘设置窗口背景色
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

app = QApplication(sys.argv)
win=QMainWindow()
win.resize(350,  250)

palette=QPalette()
palette.setColor(QPalette.Background,Qt.red)
win.setPalette(palette)

win.show()

sys.exit(app.exec_())
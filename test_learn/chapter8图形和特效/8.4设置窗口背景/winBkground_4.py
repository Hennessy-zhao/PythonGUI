# -*- coding:UTF-8 -*-
'''
使用QPalette设置窗口背景
使用QPalette调色盘设置窗口背景图片
当背景图片的宽度和高度大于窗口的宽度和高度时，背景图片会平铺整个背景
当背景图片的宽度和高度小于窗口的宽度和高度时，则会加载多个背景图片
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

app = QApplication(sys.argv)
win=QMainWindow()
#试着让屏幕的大小分别是(460,255)和(800,600)
win.resize(800,  600)

palette=QPalette()
palette.setBrush(QPalette.Background,QBrush(QPixmap("../img/python.jpg")))
win.setPalette(palette)

win.show()

sys.exit(app.exec_())
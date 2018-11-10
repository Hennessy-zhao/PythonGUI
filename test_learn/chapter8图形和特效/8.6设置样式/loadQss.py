# -*- coding:UTF-8 -*-
'''
加载QSS
QSS在style.qss文件里面
为了方便以后的调用，编写一个加载样式的公共类CommonHelper，在CommonHelper.py文件里面
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CommonHelper import CommonHelper
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(477, 258)
        self.setWindowTitle("加载QSS文件")
        btn1 = QPushButton(self)
        btn1.setText('添加')
        btn1.setToolTip('测试提示')
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)

        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()

    styleFile = './style.qss'
    qssStyle = CommonHelper.readQss(styleFile)
    win.setStyleSheet(qssStyle)
    win.show()
    sys.exit(app.exec_())

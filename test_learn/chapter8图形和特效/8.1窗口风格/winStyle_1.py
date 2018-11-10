# -*- coding:UTF-8 -*-
'''
设置窗口样式
在窗口类的__init__函数中使用self.setWindowFlags()函数
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.setGeometry(200,200,500,500)
        self.setWindowTitle("设置窗口样式例子")

        #设置无边框窗口例子
        self.setWindowFlags(Qt.FramelessWindowHint)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())

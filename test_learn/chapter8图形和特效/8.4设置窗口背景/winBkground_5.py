# -*- coding:UTF-8 -*-
'''
使用paintEvent设置窗口背景
设置背景色
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("paintEvent设置背景色")
        self.resize(500,500)
        self.move(200,200)

    def paintEvent(self, event):
        painter=QPainter(self)
        painter.setBrush(Qt.black)
        #设置背景色
        painter.drawRect(self.rect())




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())

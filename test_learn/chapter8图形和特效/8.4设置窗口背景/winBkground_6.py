# -*- coding:UTF-8 -*-
'''
使用paintEvent设置窗口背景
设置背景图片
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("paintEvent设置背景图片")
        self.resize(500,500)
        self.move(200,200)

    def paintEvent(self, event):
        painter=QPainter(self)
        pixmap=QPixmap("../img/screen1.jpg")
        #设置窗口背景图片，平铺到整个窗口，随着窗口的改变而改变
        painter.drawPixmap(self.rect(),pixmap)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())

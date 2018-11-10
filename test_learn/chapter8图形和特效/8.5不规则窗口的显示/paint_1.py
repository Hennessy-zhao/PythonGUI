# -*- coding:UTF-8 -*-
'''
不规则窗口的显示
图片素材既当遮罩层又当背景图片，通过重载paintEvent()函数绘制窗口背景
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyForm(QWidget):
    def __init__(self,parent=None):
        super(MyForm,self).__init__(parent)

        self.setWindowTitle("不规则窗口的实现例子")
        self.move(200,200)

    def paintEvent(self, event):
        painter=QPainter(self)
        painter.drawPixmap(0,0,280,390,QPixmap(r"../img/dog.jpg"))
        painter.drawPixmap(300,0,280,390,QBitmap(r"../img/dog.jpg"))




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MyForm()
    form.show()
    sys.exit(app.exec_())



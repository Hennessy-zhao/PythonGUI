# -*- coding:UTF-8 -*-
'''
为标签添加背景图片
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        self.label1=QLabel(self)
        self.label1.setToolTip('这是一个文本标签')
        self.label1.setStyleSheet("QLabel{border-image:url(../img/python.jpg)}")
        #设置标签的宽度和高度
        self.label1.setFixedWidth(476)
        self.label1.setFixedHeight(259)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



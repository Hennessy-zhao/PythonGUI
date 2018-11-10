# -*- coding:UTF-8 -*-
'''
为按钮添加背景图片
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

        self.btn1=QPushButton(self)
        self.btn1.setMaximumSize(48,48)
        self.btn1.setMinimumSize(48,48)
        #下面style里面也可以使用background-image，语法一样，但是border-image是让图片填充整个部分
        style='''
            QPushButton{
                border-radius:30px;
                border-image:url('../img/left.png');
            }
        '''
        self.btn1.setStyleSheet(style)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



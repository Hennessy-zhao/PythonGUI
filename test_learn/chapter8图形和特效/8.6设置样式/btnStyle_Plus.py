# -*- coding:UTF-8 -*-
'''
为按钮添加背景图片
为指定的按钮设置背景，调用QPushButton对象的setObjectName()为按钮设置一个名字
在QSS样式中设置了按钮的三种状态（正常按钮状态，鼠标悬停在按钮上的状态，按下按钮的状态）
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
        self.btn1.setObjectName('btn1')
        self.btn1.setMaximumSize(64,64)
        self.btn1.setMinimumSize(64,64)
        style='''
            #btn1{
                border-radius:30px;
                background-image:url('../img/left.png')
            }
            
            #btn1:hover{
                border-radius:30px;
                background-image:url('../img/leftHover.png')
            }
            
            #btn1:Pressed{
                border-radius:30px;
                background-image:url('../img/leftPressed.png')
            }
        '''
        self.btn1.setStyleSheet(style)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



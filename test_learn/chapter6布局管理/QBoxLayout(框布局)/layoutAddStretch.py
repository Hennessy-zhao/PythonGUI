# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("布局管理addStretch()函数的使用")
        self.move(200,200)

        btn1=QPushButton(self)
        btn2=QPushButton(self)
        btn3=QPushButton(self)
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')

        layout=QHBoxLayout()
        #设置伸缩量为１
        layout.addStretch(1)
        layout.addWidget(btn1)
        #设置伸缩量为１
        layout.addStretch(1)
        layout.addWidget(btn2)
        #设置伸缩量为１
        layout.addStretch(1)
        layout.addWidget(btn3)
        #设置伸缩量为１
        layout.addStretch(1)

        self.setLayout(layout)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



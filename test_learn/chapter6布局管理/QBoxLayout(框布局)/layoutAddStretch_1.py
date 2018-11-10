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
        btn4 = QPushButton(self)
        btn5 = QPushButton(self)
        btn6 = QPushButton(self)
        btn4.setText('button 4')
        btn5.setText('button 5')
        btn6.setText('button 6')

        layout=QVBoxLayout()
        layout1=QHBoxLayout()
        layout2=QHBoxLayout()

        #在layout1中令按钮组局右显示
        #设置伸缩量为１
        layout1.addStretch(1)
        layout1.addWidget(btn1)
        layout1.addWidget(btn2)
        layout1.addWidget(btn3)

        #在layout2中令按钮居左显示
        layout2.addWidget(btn4)
        layout2.addWidget(btn5)
        layout2.addWidget(btn6)
        layout2.addStretch(1)

        layout.addLayout(layout1)
        layout.addLayout(layout2)
        self.setLayout(layout)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



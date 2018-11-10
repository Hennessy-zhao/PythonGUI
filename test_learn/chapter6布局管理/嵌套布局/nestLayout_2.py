# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)

        self.setWindowTitle("嵌套布局示例")
        self.resize(700,200)
        self.move(200,200)

        #全局控件(注意参数self)，用于承载全局布局
        wwg=QWidget(self)
        #全局布局（注意参数wwg）
        w1=QHBoxLayout(wwg)
        hlayout=QHBoxLayout()
        vlayout=QVBoxLayout()
        glayout=QGridLayout()
        flayout=QFormLayout()

        #为局部布局添加控件（例如：按钮）
        hlayout.addWidget(QPushButton(str(1)))
        hlayout.addWidget(QPushButton(str(2)))
        vlayout.addWidget(QPushButton(str(3)))
        vlayout.addWidget(QPushButton(str(4)))
        glayout.addWidget(QPushButton(str(5)),0,0)
        glayout.addWidget(QPushButton(str(6)),0,1)
        glayout.addWidget(QPushButton(str(7)),1,0)
        glayout.addWidget(QPushButton(str(8)),1,1)
        flayout.addWidget(QPushButton(str(9)))
        flayout.addWidget(QPushButton(str(10)))
        flayout.addWidget(QPushButton(str(11)))
        flayout.addWidget(QPushButton(str(12)))

        #这里在局部布局中添加控件，然后将其添加到全部布局中
        w1.addLayout(hlayout)
        w1.addLayout(vlayout)
        w1.addLayout(glayout)
        w1.addLayout(flayout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MyWindow()
    form.show()
    sys.exit(app.exec_())



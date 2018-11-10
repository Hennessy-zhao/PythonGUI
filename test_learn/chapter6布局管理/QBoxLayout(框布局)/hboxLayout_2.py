# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        #水平布局按照从左到右的顺序添加按钮控件
        layout=QHBoxLayout()

        #水平居左、垂直靠上对齐
        layout.addWidget(QPushButton(str(1)),0,Qt.AlignTop)
        layout.addWidget(QPushButton(str(2)),0,Qt.AlignLeft|Qt.AlignTop)
        layout.addWidget(QPushButton(str(3)))

        #水平居左、垂直靠下对齐
        layout.addWidget(QPushButton(str(4)),0,Qt.AlignLeft)
        layout.addWidget(QPushButton(str(5)),0,Qt.AlignLeft|Qt.AlignBottom)

        self.setLayout(layout)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



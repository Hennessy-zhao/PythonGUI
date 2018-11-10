# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("垂直布局管理例子")
        self.move(200,200)

        layout=QVBoxLayout()
        layout.addWidget(QPushButton(str(1)))
        layout.addWidget(QPushButton(str(2)))
        layout.addWidget(QPushButton(str(3)))
        layout.addWidget(QPushButton(str(4)))
        layout.addWidget(QPushButton(str(5)))
        self.setLayout(layout)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



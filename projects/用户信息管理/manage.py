# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("登录")

        self.user_ID=QLineEdit()
        self.user_pad=QLineEdit()

        grid=QGridLayout()
        grid.addWidget(QLabel("账号名"),0,0)
        grid.addWidget(self.user_ID,0,1)
        grid.addWidget(QLabel("密码"),1,1)
        grid.addWidget(self.user_pad,1,1)

        vlayout=QVBoxLayout()
        vlayout.addWidget(QLabel("系统登录"),Qt.AlignCenter)
        vlayout.addLayout(grid)
        vlayout.addWidget(QPushButton("登录"),Qt.AlignCenter)

        self.setLayout(vlayout)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



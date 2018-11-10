# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)

        self.setWindowTitle("水平布局管理例子")
        self.move(200,200)

        layout=QHBoxLayout()
        layout.addWidget(QPushButton(str(1)))
        layout.addWidget(QPushButton(str(2)))
        layout.addWidget(QPushButton(str(3)))
        layout.addWidget(QPushButton(str(4)))
        layout.addWidget(QPushButton(str(5)))

        #设置控件间距
        layout.addSpacing(0)

        self.setLayout(layout)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



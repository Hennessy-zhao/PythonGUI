# -*- coding:UTF-8 -*-
'''
内置信号和槽函数

'''
from PyQt5.QtWidgets import *
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)

        self.setWindowTitle("内置信号/槽示例")
        self.resize(500,500)
        self.move(200,200)

        btn=QPushButton('关闭',self)
        btn.clicked.connect(self.close)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



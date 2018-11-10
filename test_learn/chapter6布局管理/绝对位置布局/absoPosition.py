# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
import sys

class Example(QWidget):
    def __init__(self,parent=None):
        super(Example,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("绝对位置布局例子")
        self.resize(500,500)
        self.move(200,200)

        label1=QLabel('欢迎',self)
        label1.move(15,10)

        label2=QLabel('学习',self)
        label2.move(35,40)

        label3=QLabel('PyQt5',self)
        label3.move(55,70)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Example()
    form.show()
    sys.exit(app.exec_())



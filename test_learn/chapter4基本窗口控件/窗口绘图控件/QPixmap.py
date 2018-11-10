# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)

        self.setWindowTitle("QPixmap例子")
        self.resize(500,500)
        self.move(200,200)

        layout=QVBoxLayout()

        lab1=QLabel()

        lab1.setPixmap(QPixmap("../img/python.jpg"))


        layout.addWidget(lab1)
        self.setLayout(layout)





if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



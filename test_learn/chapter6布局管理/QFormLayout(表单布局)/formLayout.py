# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)

        self.setWindowTitle("表单布局管理例子")
        self.resize(500,500)
        self.move(200,200)

        layout=QFormLayout()
        label1=QLabel('标签１')
        linEdit1=QLineEdit()
        label2=QLabel('标签２')
        linEdit2=QLineEdit()
        label3=QLabel('标签３')
        linEdit3=QLineEdit()

        layout.addRow(label1,linEdit1)
        layout.addRow(label2,linEdit2)
        layout.addRow(label3,linEdit3)

        self.setLayout(layout)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



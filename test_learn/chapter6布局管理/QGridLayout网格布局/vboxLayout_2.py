# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("故障中告")
        self.resize(500,500)
        self.move(200,200)

        title=QLabel('标题')
        author=QLabel('提交人')
        review=QLabel('中告内容')

        titleEdit=QLineEdit()
        authorEdit=QLineEdit()
        reviewEdit=QTextEdit()

        layout=QGridLayout()
        self.setLayout(layout)

        layout.setSpacing(10)

        layout.addWidget(title,1,0)
        layout.addWidget(titleEdit,1,1)

        layout.addWidget(author,2,0)
        layout.addWidget(authorEdit,2,1)

        layout.addWidget(review,3,0)
        layout.addWidget(reviewEdit,3,1,5,1)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



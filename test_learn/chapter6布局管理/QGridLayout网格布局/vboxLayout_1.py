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
        self.setWindowTitle("网格布局管理例子")
        self.move(200,200)

        layout=QGridLayout()
        self.setLayout(layout)

        names=['Cls','Back',' ','Close','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']

        positions=[(i,j) for i in range(5) for j in range(4)]

        for position,name in zip(positions,names):
            if name==' ':
                continue
            button=QPushButton(name)
            layout.addWidget(button,*position)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



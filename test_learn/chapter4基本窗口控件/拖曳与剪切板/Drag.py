# -*- coding:UTF-8 -*-
#拖曳
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Combo(QComboBox):
    def __init__(self,title,parent):
        super(Combo,self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):     #e是被操作的窗口控件
        print(e)
        #print(e.mimeData().hasText())      当有数据的时候，返回的是True
        if e.mimeData().hasText():
            e.accept()
        else :
            e.ignore()

    def dropEvent(self,e):
        self.addItem(e.mimeData().text())



class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("简单的拖曳例子")
        self.resize(500,500)
        self.move(200,200)

        lo=QFormLayout()
        lo.addRow(QLabel("请把左边的文本拖曳到右边的下拉菜单中"))
        edit=QLineEdit()
        edit.setDragEnabled(True)
        com=Combo("Button",self)    #这个Button对应的是Combo类init的title，也可以把Button和title同时去掉
        lo.addRow(edit,com)
        self.setLayout(lo)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Example()
    form.show()
    sys.exit(app.exec_())



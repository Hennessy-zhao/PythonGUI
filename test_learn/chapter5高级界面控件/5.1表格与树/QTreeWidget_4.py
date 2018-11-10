# -*- coding:UTF-8 -*-
#树形控件中使用系统的定制模式
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class TreeWidgetDemo(QMainWindow):
    def __init__(self,parent=None):
        super(TreeWidgetDemo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        #系统提供的模式
        model=QDirModel()
        #创建一个QTreeView控件
        tree=QTreeView()
        #为控件添加模式
        tree.setModel(model)

        self.setCentralWidget(tree)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=TreeWidgetDemo()
    form.show()
    sys.exit(app.exec_())



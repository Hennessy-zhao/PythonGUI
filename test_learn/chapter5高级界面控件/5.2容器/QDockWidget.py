# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo,self).__init__(parent)

        self.setWindowTitle("Dock 例子")
        self.resize(500,500)
        self.move(200,200)



        #设置菜单栏
        bar=self.menuBar()
        file=bar.addMenu("File")
        file.addAction("New")
        file.addAction("save")
        file.addAction("quit")

        #创建可停靠的窗口items
        self.items=QDockWidget("Dockable",self)
        self.listWidget=QListWidget()
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        self.items.setWidget(self.listWidget)
        #设置窗口是否可以浮动
        self.items.setFloating(False)

        #在MainWindow中间添加控件QtextEdit()
        self.setCentralWidget(QTextEdit())

        #将停靠小窗口放在中央控件右侧
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=DockDemo()
    form.show()
    sys.exit(app.exec_())



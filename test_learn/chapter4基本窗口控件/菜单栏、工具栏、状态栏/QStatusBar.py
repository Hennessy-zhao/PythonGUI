# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class StatusDemo(QMainWindow):
    def __init__(self,parent=None):
        super(StatusDemo,self).__init__(parent)

        self.setWindowTitle("QStatusBar例子")
        self.resize(500,500)
        self.move(200,200)

        bar=self.menuBar()
        file=bar.addMenu("File")
        file.addAction("show")
        file.triggered[QAction].connect(self.processTrigger)
        self.setCentralWidget(QTextEdit())

        #通过主窗口的QMainWindow的setStatusBar()函数设置状态栏
        self.statusBar=QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("菜单的内容")

    def processTrigger(self,q):
        if (q.text()=="show"):
            self.statusBar.showMessage(q.text()+"菜单选项被点击了",5000)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=StatusDemo()
    form.show()
    sys.exit(app.exec_())



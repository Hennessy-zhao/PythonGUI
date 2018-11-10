# -*- coding:UTF-8 -*-
#多重文档界面。在PyQt5的窗口中使用QMdiArea控件
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
    count=0
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        #MidArea控件
        self.mdi=QMdiArea()
        self.setCentralWidget(self.mdi)

        #菜单栏
        bar=self.menuBar()
        file=bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.windowaction)

    def windowaction(self,q):
        print("triggered")

        #选择菜单中的new，则添加一个新的ＭＤＩ，主窗口内部会增加ＭＤＩ的数量
        if q.text()=='New':
            MainWindow.count=MainWindow.count+1
            sub=QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow"+str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        #选择菜单中的csacsde和tiled，会在主窗口中显示子窗口的排列方式：级联显示子窗口或者平铺显示子窗口
        if q.text()=='cascade':
            self.mdi.cascadeSubWindows()
        if q.text()=='Tiled':
            self.mdi.tileSubWindows()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())



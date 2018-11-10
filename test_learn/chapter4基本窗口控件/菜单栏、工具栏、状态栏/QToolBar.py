# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class ToolBarDemo(QMainWindow):
    def __init__(self,parent=None):
        super(ToolBarDemo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        layout=QVBoxLayout()

        tb=self.addToolBar("File")
        new=QAction(QIcon("../img/new.png"),"new",self)
        tb.addAction(new)

        open=QAction(QIcon("../img/open.png"),"open",self)
        tb.addAction(open)

        save=QAction(QIcon("../img/save.png"),"save",self)
        #设置快捷键
        save.setShortcut("Ctrl+S")
        tb.addAction(save)

        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

        self.setLayout(layout)

    def toolbtnpressed(self,a):
        print("pressed tool button is",a.text())


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=ToolBarDemo()
    form.show()
    sys.exit(app.exec_())



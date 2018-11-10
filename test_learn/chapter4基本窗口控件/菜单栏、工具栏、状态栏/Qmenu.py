# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MenuDemo(QMainWindow):
    def __init__(self,parent=None):
        super(MenuDemo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)


        layout=QHBoxLayout()
        bar=self.menuBar()      #返回主窗口的QMenuBar对象
        file=bar.addMenu("File")
        file.addAction("New")

        save=QAction("Save",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        edit=file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

        quit=QAction("Quit",self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.processtrigger)

        self.setLayout(layout)

    def processtrigger(self,q):
        print(q.text()+" is triggered")




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MenuDemo()
    form.show()
    sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import qdarkstyle

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        layout=QHBoxLayout()
        self.setLayout(layout)
        btn=QPushButton("Button1")
        layout.addWidget(btn)
        btn.clicked.connect(self.onclickBtn)

    def onclickBtn(self):
        QMessageBox.about(self,'标题','关于对话框关于对话框关于对话框关于对话框关于对话框')




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form.show()
    sys.exit(app.exec_())
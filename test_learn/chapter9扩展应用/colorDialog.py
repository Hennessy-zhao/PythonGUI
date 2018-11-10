# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class ColorDialog(QWidget):
    def __init__(self,parent=None):
        super(ColorDialog,self).__init__(parent)
        self.setWindowTitle("颜色选择")
        self.resize(500,500)
        self.move(200,200)
        color=QColor(0,0,0)
        self.button=QPushButton('Dialog',self)
        self.button.setFocusPolicy(Qt.NoFocus)
        self.button.move(20,20)
        self.button.clicked.connect(self.showDialog)
        self.setFocus()
        self.widgt=QWidget(self)
        self.widgt.setStyleSheet('QWidget{background-color:%s}'%color.name())
        self.widgt.setGeometry(130,22,100,100)

    def showDialog(self):
        col=QColorDialog.getColor()
        if col.isValid():
            self.widgt.setStyleSheet('QWidget{background-color:%s}'%col.name())



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=ColorDialog()
    form.show()
    sys.exit(app.exec_())



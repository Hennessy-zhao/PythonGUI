# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Example(QWidget):
    def __init__(self,parent=None):
        super(Example,self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QScrollBar例子")
        self.resize(500,500)
        self.move(200,200)

        hbox=QHBoxLayout()
        self.l1=QLabel("拖动滑块改变颜色")
        self.l1.setFont(QFont("Arial",16))
        hbox.addWidget(self.l1)

        self.s1=QScrollBar()
        self.s1.setMaximum(255)
        self.s1.sliderMoved.connect(self.sliderval)

        self.s2=QScrollBar()
        self.s2.setMaximum(255)
        self.s2.sliderMoved.connect(self.sliderval)

        self.s3=QScrollBar()
        self.s3.setMaximum(255)
        self.s3.sliderMoved.connect(self.sliderval)

        hbox.addWidget(self.s1)
        hbox.addWidget(self.s2)
        hbox.addWidget(self.s3)

        self.setLayout(hbox)

    def sliderval(self):
        print(self.s1.value(),self.s2.value(),self.s3.value())

        #设置字体颜色
        palette=QPalette()
        c=QColor(self.s1.value(),self.s2.value(),self.s3.value(),255)
        palette.setColor(QPalette.Foreground,c)
        self.l1.setPalette(palette)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Example()
    form.show()
    sys.exit(app.exec_())



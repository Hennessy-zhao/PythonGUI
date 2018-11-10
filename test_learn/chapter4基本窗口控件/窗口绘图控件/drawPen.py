# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Drawing(QWidget):
    def __init__(self,parent=None):
        super(Drawing,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("钢笔样式例子")
        self.setGeometry(300,300,500,500)

    def paintEvent(self,e):
        qp=QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self,qp):
        pen=QPen(QColor(100,200,34),2,Qt.SolidLine)     #这里的QColor(100,200,34)也可以写成Qt.red,Qt.black之类的

        qp.setPen(pen)
        qp.drawLine(20,40,400,40)

        pen.setStyle(Qt.DashLine)
        #pen.setColor(Qt.red)
        qp.setPen(pen)
        qp.drawLine(20,80,250,80)

        pen.setStyle(Qt.DashDotLine)
        qp.setPen(pen)
        qp.drawLine(20,120,250,120)

        pen.setStyle(Qt.DotLine)
        qp.setPen(pen)
        qp.drawLine(20,160,250,160)

        pen.setStyle(Qt.DashDotDotLine)
        qp.setPen(pen)
        qp.drawLine(20,200,250,200)

        #创建线条样式
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,10,5,4])  #含义为1像素宽度的横线，10像素宽度的空格，5像素宽度的横线，4像素宽度的距离
        qp.setPen(pen)
        qp.drawLine(20,240,250,240)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Drawing()
    form.show()
    sys.exit(app.exec_())



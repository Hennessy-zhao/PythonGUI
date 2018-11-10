# -*- coding:UTF-8 -*-

#绘制点
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys,math


class Drawing(QWidget):
    def __init__(self,parent=None):
        super(Drawing,self).__init__(parent)

        self.setWindowTitle("在窗口中画点")
        self.resize(500,500)
        self.move(200,200)

    def paintEvent(self,event):
        #初始化绘图工具
        qp = QPainter()
        #开始在窗口中绘制
        qp.begin(self)
        #自定义画点方法
        self.drawPoints(qp)
        #结束在窗口中绘制
        qp.end()

    def drawPoints(self,qp):
        qp.setPen(Qt.red)
        size=self.size()

        for i in range(1000):
            #绘制正弦函数图形，它的周期是[-100,100]
            x=100*(-1+2.0*i/1000)+size.width()/2.0
            y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0
            qp.drawPoint(x,y)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Drawing()
    form.show()
    sys.exit(app.exec_())



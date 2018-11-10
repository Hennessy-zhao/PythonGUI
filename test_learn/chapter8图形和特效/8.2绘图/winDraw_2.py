# -*- coding:UTF-8 -*-
'''
演示绘制矩形的功能
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle("绘制矩形例子")

        self.pix=QPixmap()
        self.lastPoint=QPoint()
        self.endPoint=QPoint()
        self.initUI()

    def initUI(self):
        #设置窗口大小为600*500
        self.resize(600,500)
        #设置画布大小为400*400,背景为白色
        self.pix=QPixmap(400,400)
        self.pix.fill(Qt.white)

    #1
    def paintEvent(self, event):
        painter=QPainter(self)
        x=self.lastPoint.x()
        y=self.lastPoint.y()
        w=self.endPoint.x()-x
        h=self.endPoint.y()-y

        pp=QPainter(self.pix)
        pp.drawRect(x,y,w,h)
        painter.drawPixmap(0,0,self.pix)

    def mousePressEvent(self, event):
        #按下鼠标左键
        if event.button()==Qt.LeftButton:
            self.lastPoint=event.pos()
            self.endPoint=self.lastPoint

    def mouseMoveEvent(self, event):
        #然后移动鼠标指针
        if event.buttons() and Qt.LeftButton:
            self.endPoint=event.pos()
            #进行重新绘制
            self.update()

    def mouseReleaseEvent(self, event):
        #释放鼠标左键
        if event.button()==Qt.LeftButton:
            self.endPoint=event.pos()
            #进行重新绘制
            self.update()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())
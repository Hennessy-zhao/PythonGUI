# -*- coding:UTF-8 -*-
'''
不规则窗口实现动画效果
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class ShapeWidget(QWidget):
    def __init__(self,parent=None):
        super(ShapeWidget,self).__init__(parent)

        self.setWindowTitle("不规则窗口的动画效果")
        self.i=1
        self.mypix()
        self.timer=QTimer()
        #定时器每５００毫秒更新一次
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timeChange)
        self.timer.start()

    #显示不规则图片
    def mypix(self):
        self.update()
        if self.i==5:
            self.i=1
        self.mypic={
            1:'../img/left.png',
            2:'../img/up.png',
            3:'../img/right.png',
            4:'../img/down.png'
        }
        self.pix=QPixmap(self.mypic[self.i],"0",Qt.AvoidDither | Qt.ThresholdDither | Qt.ThresholdAlphaDither)
        self.resize(self.pix.size())
        self.setMask(self.pix.mask())
        self.dragPosition=None

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
        elif event.button()==Qt.RightButton:
            self.close()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self,QMouseEvent):
        self.m_drag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def paintEvent(self, event):
        painter=QPainter(self)
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),self.pix)

    #鼠标双击事件
    def mouseDoubleClickEvent(self, event):
        if event.button()==1:
            self.i+=1
            self.mypix()

    #每５００毫秒窗口执行一次更新操作，重绘窗口
    def timeChange(self):
        self.i+=1
        self.mypix()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=ShapeWidget()
    form.show()
    sys.exit(app.exec_())



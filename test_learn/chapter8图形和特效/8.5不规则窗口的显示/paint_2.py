# -*- coding:UTF-8 -*-
'''
不规则窗口的显示
使用一张遮罩层图片来控制窗口的大小，再利用paintEvent()函数重绘窗口的背景图等
本例使用的素材图片为mask.png和screen1.jpg
该窗口无法拖动
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Winform(QWidget):
    def __init__(self,parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("不规则窗口的实现例子")

        self.pix=QBitmap("../img/mask.png")
        self.resize(self.pix.size())
        self.setMask(self.pix)

    def paintEvent(self, event):
        painter=QPainter(self)
        #在指定区域直接绘制窗口背景
        painter.drawPixmap(0,0,self.pix.width(),self.pix.height(),QPixmap("../img/screen1.jpg"))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Winform()
    form.show()
    sys.exit(app.exec_())



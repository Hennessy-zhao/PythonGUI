# -*- coding:UTF-8 -*-
'''
缩放图片
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)
        #filename为图片的路径
        filename=r"../img/Cloudy_72px.png"
        img=QImage(filename)

        #设置标签的宽度为120像素，高度为120像素，所加载的图片按照标签的高度和宽度等比例缩放
        label1=QLabel(self)
        label1.setFixedWidth(120)
        label1.setFixedHeight(120)
        #缩放图片，以固定大小显示
        result=img.scaled(label1.width(),label1.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        #在标签控件上显示图片
        label1.setPixmap(QPixmap.fromImage(result))



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



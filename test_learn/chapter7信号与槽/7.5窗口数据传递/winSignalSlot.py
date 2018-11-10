# -*- coding:UTF-8 -*-
'''
单一窗口数据传递
利用信号与槽机制非常容易解决
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setWindowTitle("信号与槽：连接滑块LCD")
        self.resize(500,500)
        self.move(200,200)

        #先创建滑块和LCD控件
        lcd=QLCDNumber(self)
        slide=QSlider(Qt.Horizontal,self)

        vBox=QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slide)

        self.setLayout(vBox)

        #valueChanged()是QSlider的一个信号函数，
        # 只要slider的值发生改变，他就会发射一个信号
        #然后通过connect连接信号的接收控件，也就是lcd
        slide.valueChanged.connect(lcd.display)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



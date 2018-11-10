# -*- coding:UTF-8 -*-
#QSlider滑动条的水平案例
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class SliderDemo(QWidget):
    def __init__(self,parent=None):
        super(SliderDemo,self).__init__(parent)

        self.setWindowTitle("QSlider滑动条")
        self.resize(500,500)
        self.move(200,200)

        layout=QVBoxLayout()
        self.l1=QLabel("Hello PyQt5")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        #水平方向
        self.s1=QSlider(Qt.Horizontal)
        #设置最小值
        self.s1.setMinimum(10)
        #设置最大值
        self.s1.setMaximum(50)
        #步长
        self.s1.setSingleStep(2)
        #设置当前值
        self.s1.setValue(20)
        #刻度位置，刻度在下方
        self.s1.setTickPosition(QSlider.TicksBelow)
        #设置刻度间隔
        self.s1.setTickInterval(2)

        layout.addWidget(self.s1)

        #链接信号槽
        self.s1.valueChanged.connect(self.valueChange)

        self.setLayout(layout)

    def valueChange(self):
        print("current slider value=%s"%self.s1.value())
        size=self.s1.value()
        self.l1.setFont(QFont("Arial",size))




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=SliderDemo()
    form.show()
    sys.exit(app.exec_())



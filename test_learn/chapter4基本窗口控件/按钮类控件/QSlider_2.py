# -*- coding:UTF-8 -*-
#QSlider滑动条的竖直案例
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

        layout=QHBoxLayout()

        self.l1=QLabel("Hello Word!!")
        self.l1.setAlignment(Qt.AlignLeft)
        self.l1.setFont(QFont("Arial",20))
        layout.addWidget(self.l1)

        #垂直方向
        self.s1=QSlider(Qt.Vertical)
        #设置最小值
        self.s1.setMinimum(10)
        #设置最大值
        self.s1.setMaximum(50)
        #设置步长
        self.s1.setSingleStep(2)
        #设置滑动条的值
        self.s1.setValue(20)
        #设置刻度间隔
        self.s1.setTickInterval(2)
        #设置刻度位置（设置为左边）
        self.s1.setTickPosition(QSlider.TicksLeft)
        #设置链接信号槽
        self.s1.valueChanged.connect(self.valueChange)

        layout.addWidget(self.s1)
        self.setLayout(layout)

    def valueChange(self):
        print("current Value:",self.s1.value())
        self.l1.setFont(QFont("Arial",int(self.s1.value())))



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



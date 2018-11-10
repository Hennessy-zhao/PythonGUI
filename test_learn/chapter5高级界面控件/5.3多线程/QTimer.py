# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)

        self.setWindowTitle("QTimer demo")
        self.resize(500,500)
        self.move(200,200)

        layout=QGridLayout(self)
        self.listFile=QListWidget()
        self.label=QLabel("显示当前时间")
        self.startButton=QPushButton("开始")
        self.stopButton=QPushButton('结束')
        layout.addWidget(self.label,0,0,1,2)
        layout.addWidget(self.startButton,1,0)
        layout.addWidget(self.stopButton,1,1)

        #初始化一个定时器
        self.timer=QTimer(self)
        #showTime方法
        self.timer.timeout.connect(self.showTime)

        self.startButton.clicked.connect(self.startTimer)
        self.stopButton.clicked.connect(self.stopTimer)

        self.setLayout(layout)

    def showTime(self):
        #获取系统现在的时间
        time=QDateTime.currentDateTime()
        #设置系统时间显示格式
        timeDisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")
        #在标签上显示时间
        self.label.setText("显示当前时间："+timeDisplay)

    def startTimer(self):
        #设置时间间隔并启动定时器，相当于每隔１ｓ就启动一次，就出发一次timeout
        self.timer.start(1000)
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)

    def stopTimer(self):
        self.timer.stop()
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



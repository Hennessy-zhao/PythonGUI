# -*- coding:UTF-8 -*-
'''
在界面中分离ＵＩ主线程与工作线程
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

global sec
sec=0


class WorkThread(QThread):
    trigger=pyqtSignal()
    def __init__(self):
        super(WorkThread,self).__init__()

    def run(self):
        for i in range(2000000000):
            pass
        #循环完成后发射信号

        self.trigger.emit()

def countTime():
    global sec
    sec+=1
    #LED显示数字＋１
    lcdNumber.display(sec)

def work():
    #计时器每秒计数
    timer.start(1000)
    #计时开始
    workThread.start()
    workThread.trigger.connect(timeStop)

def timeStop():
    timer.stop()
    print("运行结束用时",lcdNumber.value())
    global sec
    sec=0


if __name__=='__main__':
    app=QApplication(sys.argv)
    top=QWidget()
    top.resize(500,500)

    #垂直布局类QVBoxLayout
    layout=QVBoxLayout()
    #添加一个显示面板
    lcdNumber=QLCDNumber()
    layout.addWidget(lcdNumber)
    button=QPushButton("测试")
    layout.addWidget(button)

    timer=QTimer()
    workThread=WorkThread()

    button.clicked.connect(work)
    #每次计时结束，触发countTime
    timer.timeout.connect(countTime)

    top.setLayout(layout)
    top.show()

    sys.exit(app.exec_())



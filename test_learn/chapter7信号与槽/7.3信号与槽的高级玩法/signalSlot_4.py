# -*- coding:UTF-8 -*-
'''
多线程中信号与槽的使用
秀简单的多线程使用方法是使用QThread函数
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Main(QWidget):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)

        self.setWindowTitle("多线程的使用方法")
        self.resize(500,500)
        self.move(200,200)

        #创建一个线程实例并设置名称、变量、信号与槽
        self.thread=MyThread()
        self.thread.setIdentity("thread1")
        self.thread.sinOut.connect(self.outText)
        self.thread.setVal(6)

    def outText(self,text):
        print(text)


class MyThread(QThread):
    sinOut=pyqtSignal(str)

    def __init__(self,parent=None):
        super(MyThread,self).__init__(parent)
        self.identity=None

    def setIdentity(self,text):
        self.identity=text

    def setVal(self,val):
        self.times=int(val)
        #执行县城的run方法
        self.start()

    def run(self):
        while self.times>0 and self.identity:
            #发射信号
            self.sinOut.emit(self.identity+"==>"+str(self.times))
            self.times-=1




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Main()
    form.show()
    sys.exit(app.exec_())



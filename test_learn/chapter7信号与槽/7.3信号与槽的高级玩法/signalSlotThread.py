# -*- coding:UTF-8 -*-
'''
多线程
使用主线程更新界面，使用子线程实时处理数据，最后将结果显示到界面上
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time

class BackendThread(QThread):
    #通过类成员对象定义信号
    update_date=pyqtSignal(str)

    #处理业务逻辑
    def run(self):
        while True:
            data=QDateTime.currentDateTime()
            currTime=data.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currTime))
            time.sleep(1)

class Window(QDialog):
    def __init__(self,parent=None):
        super(Window,self).__init__(parent)

        self.setWindowTitle("PyQt5界面实时更新例子")
        self.move(200,200)
        self.input=QLineEdit(self)
        self.input.resize(400,100)
        self.initUI()

    def initUI(self):
        #创建线程
        self.backend=BackendThread()
        #连接信号
        self.backend.update_date.connect(self.handleDisplay)
        #开始线程
        self.backend.start()

    #将当前时间输出到文本框
    def handleDisplay(self,data):
        self.input.setText(data)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Window()
    form.show()
    sys.exit(app.exec_())



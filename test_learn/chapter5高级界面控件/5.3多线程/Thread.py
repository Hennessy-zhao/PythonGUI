# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWidget(QWidget):
    def __init__(self,parent=None):
        super(MainWidget,self).__init__(parent)

        self.setWindowTitle("QThread例子")
        self.resize(500,500)
        self.move(200,200)

        self.thread=Worker()
        self.listFile=QListWidget()
        self.btnStart=QPushButton('开始')
        layout=QGridLayout(self)
        layout.addWidget(self.listFile,0,0,1,2)
        layout.addWidget(self.btnStart,1,1)
        self.btnStart.clicked.connect(self.slotStart)
        self.thread.sinOut.connect(self.slotAdd)

    def slotAdd(self,file_inf):
        self.listFile.addItem(file_inf)

    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.thread.start()


class Worker(QThread):
    sinOut=pyqtSignal(str)

    def __init__(self,parent=None):
        super(Worker,self).__init__(parent)
        self.working=True
        self.num=0

    def __del__(self):
        self.working=False
        self.wait()

    def run(self):
        while self.working==True:
            file_str='File index {0}'.format(self.num)   #也可以写成file_str = 'File index'+str(self.num)

            self.num+=1
            #发射信号
            self.sinOut.emit(file_str)
            #线程休眠２秒
            self.sleep(2)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MainWidget()
    form.show()
    sys.exit(app.exec_())



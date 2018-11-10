# -*- coding:UTF-8 -*-
'''
使用processEvent()函数，在主函数执行耗时操作的地方，加入QApplication.processEvent()

'''

from PyQt5.QtWidgets import *
import sys
import time

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle("实时刷新页面例子")
        self.move(200,200)

        self.listFile=QListWidget()
        self.btnstart=QPushButton('开始')
        layout=QGridLayout(self)
        layout.addWidget(self.listFile,0,0,1,2)
        layout.addWidget(self.btnstart,1,1)
        self.btnstart.clicked.connect(self.slotAdd)
        self.setLayout(layout)

    def slotAdd(self):
        for n in range(10):
            str_n='File index {0}'.format(n)
            self.listFile.addItem(str_n)
            self.btnstart.setText(str(n))
            QApplication.processEvents()
            time.sleep(1)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



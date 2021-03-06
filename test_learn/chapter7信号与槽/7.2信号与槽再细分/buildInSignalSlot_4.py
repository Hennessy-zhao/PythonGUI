# -*- coding:UTF-8 -*-
'''
自定义信号和槽函数

'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class WinForm(QWidget):
    #自定义信号，不带参数
    button_clicked_signal=pyqtSignal()

    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)

        self.setWindowTitle("自定义信号和槽函数示例")
        self.resize(500,500)
        self.move(200,200)

        btn=QPushButton('关闭',self)
        #连接信号与槽函数
        btn.clicked.connect(self.btn_clicked)
        #接收信号，连接到自定义槽函数
        self.button_clicked_signal.connect(self.btn_close)

    def btn_clicked(self):
        #发送自定义信号，无参数
        self.button_clicked_signal.emit()

    def btn_close(self):
        self.close()




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



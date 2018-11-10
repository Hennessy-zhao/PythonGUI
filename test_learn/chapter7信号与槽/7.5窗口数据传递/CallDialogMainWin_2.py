# -*- coding:UTF-8 -*-
'''
调用transParam_DateDialog_2.py的主页面
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from transParam_DateDialog_2 import DateDialog
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("信号与槽传递参数的示例")

        self.open_btn=QPushButton('获取时间')
        self.lineEdit_inner=QLineEdit(self)
        self.lineEdit_emit=QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)

        self.lineEdit_inner.setText('接收子窗口内置信号的时间')
        self.lineEdit_emit.setText('接收子窗口自定义信号的时间')

        grid=QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)

        grid.addWidget(self.open_btn)
        self.setLayout(grid)

    def openDialog(self):
        dialog=DateDialog(self)
        '''连接子窗口的内置信号与主窗口的槽函数'''
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        '''连接子窗口的自定义信号与主窗口的槽函数'''
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)
        dialog.show()

    def deal_inner_slot(self,date):
        self.lineEdit_inner.setText(date.toString())

    def deal_emit_slot(self,dateStr):
        self.lineEdit_emit.setText(dateStr)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())
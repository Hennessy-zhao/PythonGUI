# -*- coding:UTF-8 -*-
'''
多窗口数据传递---在自定义对话框之间通过属性传参
该文件为一个自定义对话框，为一个子窗口，调用子窗口的属性的主窗口是CallDialogMainWin.py
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class DateDialog(QDialog):
    def __init__(self,parent=None):
        super(DateDialog,self).__init__(parent)
        self.setWindowTitle("DateDialog")

        #在布局中添加控件
        layout=QVBoxLayout(self)
        self.datetime=QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.datetime)

        #使用两个按钮（Ok和Cancel）分别连接accept()和reject()槽函数
        buttons=QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    #从对话框中获取当前日期和时间
    def dateTime(self):
        return self.datetime.dateTime()

    #使用静态函数创建对话框并返回(date,time,accepted)
    @staticmethod
    def getDateTime(parent=None):
        dialog=DateDialog(parent)
        result=dialog.exec_()
        #通过dialog.exec_()返回值判断用户单机的是Ok还是Cancel按钮
        date=dialog.dateTime()
        return  (date.date(),date.time(),result==QDialog.Accepted)
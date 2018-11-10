# -*- coding:UTF-8 -*-
'''
调用transParam_DateDialog.py对话框窗口的主窗口
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from transParam_DateDialog import DateDialog
import sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("对话框关闭时返回值给主窗口例子")

        self.lineEdit=QLineEdit(self)
        self.button1=QPushButton('弹出对话框１')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2=QPushButton("弹出对话框２")
        self.button2.clicked.connect(self.onButton2Click)

        gridLayout=QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog=DateDialog(self)
        result=dialog.exec_()
        date=dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print("\n日期对话框的返回值")
        print("date=%s"% str(date.date()))
        print("time=%s"% str(date.time()))
        print("result=%s"% result)
        dialog.destroy()

    def onButton2Click(self):
        date,time,result=DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print("\n日期对话框的返回值")
        print("date=%s "%str(date))
        print("time=%s"% str(time))
        print("result=%s"% result)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())
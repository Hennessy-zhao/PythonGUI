# -*- coding:UTF-8 -*-
'''
内置信号与槽的使用

'''

from PyQt5.QtWidgets import *
import sys

app=QApplication([])
widget=QWidget()
widget.setGeometry(200,200,500,500)

def showMsg():
    QMessageBox.information(widget,'信息提示框','OK,弹出测试信息')

btn=QPushButton("测试点击按钮",widget)

btn.clicked.connect(showMsg)

widget.show()
sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
'''
开发一个自定义的无边框窗口，占用１００％的用户显示屏幕
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

'''自定义窗口类'''
class MyWindow(QMainWindow):
    '''构造函数'''
    def __init__(self,parent=None):
        '''调用父类的构造函数'''
        super(MyWindow,self).__init__(parent)

        #设置窗口标志（无边框）
        self.setWindowFlags(Qt.FramelessWindowHint)

        #为便于显示，设置窗口背景颜色（采用QSS）
        self.setStyleSheet('''background-color:blue;''')

    '''最大化窗口'''
    def showMaximized(self):
        #得到桌面控件
        desktop=QApplication.desktop()
        #得到屏幕可显示尺寸
        rect=desktop.availableGeometry()
        #设置窗口尺寸
        self.setGeometry(rect)
        #显示窗口
        self.show()

#主函数
if __name__ == '__main__':
    #声明变量
    app=QApplication(sys.argv)
    #创建窗口
    window=MyWindow()
    #调用最大化显示函数
    window.showMaximized()
    #应用程序事件循环
    sys.exit(app.exec_())
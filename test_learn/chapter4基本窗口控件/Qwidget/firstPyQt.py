# -*- coding:UTF-8 -*-
#上面一行是避免生成的PyQt文件出现中文乱码

#建立一个主窗口

#载入必要的模块，Qt5中使用的基本GUI窗口控件都在PyQt5.QtWidgets中
from PyQt5.QtWidgets import QApplication ,QWidget
import sys

#每一个程序都要有一个QApplication对象，QApplication类包含在QTWidgets模块中
app=QApplication(sys.argv)      #sys.argv是一个命令行参数列表

#QWidget控件是PyQt5所有用户界面的父类，这里没有继承其他类。
window=QWidget()

#改变窗口控件的大小
window.resize(500,500)

#设置窗口初始化的位置(x,y)
window.move(200,200)

#设置窗口控件的标题，该标题在窗口标题栏中显示
window.setWindowTitle("第一个主窗口程序")

#将窗口控件显示在屏幕上
window.show()

#q确保程序完整的结束
sys.exit(app.exec_())
# -*- coding:UTF-8 -*-
'''
演示在QWebEngineView中加载本地的Web页面
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.setWindowTitle("加载并显示本地页面例子")
        self.setGeometry(5,30,555,330)

        self.brower=QWebEngineView()
        #加载本地页面

        #url=r'/usr/bin/python3.5 /home/hennessy/Python/PythonGUI/test/chapter5高级界面控件/5.4网页交互/index.html'
        #self.brower.load(QUrl(url))
        self.brower.load(QUrl.fromLocalFile('/home/hennessy/Python/PythonGUI/test/chapter5高级界面控件/5.4网页交互/index.html'))
        self.setCentralWidget(self.brower)
        programPath=str(sys.prefix)
        print('相对路径',programPath)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form= MainWindow()
    form.show()
    sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
'''
把html文件嵌入到PyQt5脚本中
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
        self.setGeometry(5,30,1355,730)
        self.browser=QWebEngineView()
        #加载ＨＴＭＬ代码
        self.browser.setHtml('''
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1 style="color:red;">11111111</h1>
</body>
</html>
        ''')
        self.setCentralWidget(self.browser)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())



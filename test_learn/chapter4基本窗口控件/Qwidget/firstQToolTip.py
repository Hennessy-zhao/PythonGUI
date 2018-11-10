# -*- coding:UTF-8 -*-

from PyQt5.QtWidgets import QApplication,QWidget,QToolTip
from PyQt5.QtGui import QFont
import  sys

class WinForm(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.initUI()


    def initUI(self):
        # 设置气泡提示
        #设置气泡提示信息的字体与字号大小
        QToolTip.setFont(QFont('SansSerif',10))

        # 创建工具提示，需要调用setToolTip()方法，该方法接受富文本格式的参数
        self.setToolTip('这是一个<b>气泡提示<b>')
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("气泡提示Demo")


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())
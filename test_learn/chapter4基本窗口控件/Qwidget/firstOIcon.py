# -*- conding:UTF-8 -*-

from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QIcon
import sys

#创建一个名为Icon的窗口类，继承自QWidget类
class Icon(QWidget):
    def __init__(self,parent=None):
        super(Icon,self).__init__(parent)
        self.initUI()


    #初始化窗口方法
    def initUI(self):
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("程序图标")
        self.setWindowIcon(QIcon('../img/cartoon1.ico'))


if __name__=='__main__':
    app=QApplication(sys.argv)
    icon=Icon()
    icon.show()
    sys.exit(app.exec_())

# -*- coding:UTF-8 -*-
#弹出一个窗口，窗口在１０ｓ后消失
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QMainWindow):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        label=QLabel("窗口会在１０s后消失")
        label.setWindowFlags(Qt.SplashScreen|Qt.FramelessWindowHint)
        self.setCentralWidget(label)






if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    label = QLabel("窗口会在１０s后消失")
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()

    QTimer.singleShot(10000, app.quit)
    sys.exit(app.exec_())



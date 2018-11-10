# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
import sys

class WindowDemo(QWidget):
    def __init__(self,parent=None):
        super(WindowDemo,self).__init__(parent)

        self.setWindowTitle("QSS样式")
        self.resize(500,500)
        self.move(200,200)

        btn1=QPushButton(self)
        btn1.setText("按钮１")

        btn2=QPushButton(self)
        btn2.setText("按钮２")

        vbox=QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        self.setLayout(vbox)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WindowDemo()
    qssStyle='''
            QPushButton{
                background-color:red;
                color:white
            }
    '''
    form.setStyleSheet(qssStyle)

    form.show()
    sys.exit(app.exec_())



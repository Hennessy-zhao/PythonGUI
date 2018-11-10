# -*- coding:UTF-8 -*-
'''
使用自定义参数
自定义参数传递方法１－－－lambda
'''
from PyQt5.QtWidgets import *
import sys

class WinForm(QMainWindow):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)

        self.setWindowTitle("自定义参数传递--lambda")
        self.resize(500,500)
        self.move(200,200)

        button1=QPushButton('Button1')
        button2=QPushButton('Button2')

        button1.clicked.connect(lambda: self.onButtonClick(1))
        button2.clicked.connect(lambda: self.onButtonClick(2))

        layout=QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        main_frame=QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self,n):
        print("Button{0} 被按下了".format(n))
        QMessageBox.information(self,"信息提示框",'Button {0} clicked'.format(n))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
'''
通过装饰器的方法来定义信号和槽函数
'''
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys

class CusWidget(QWidget):
    def __init__(self,parent=None):
        super(CusWidget,self).__init__(parent)

        self.setWindowTitle("装饰器信号与槽")
        self.resize(500,500)
        self.move(200,200)

        self.okButton=QPushButton("OK",self)
        #使用setObjectName设置对象名称
        self.okButton.setObjectName("okButton")
        layout=QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)

        #根据信号名称自动连接槽函数的核心代码
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print('单击了ＯＫ按钮')



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=CusWidget()
    form.show()
    sys.exit(app.exec_())



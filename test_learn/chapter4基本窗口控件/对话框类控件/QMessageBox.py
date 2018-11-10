# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super(MyWindow,self).__init__(parent)

        self.setWindowTitle("QMessageBox例子")
        self.resize(500,500)
        self.move(200,200)

        layout=QHBoxLayout()

        #消息对话框
        self.myButton1=QPushButton(self)
        self.myButton1.setText("消息对话框")
        self.myButton1.clicked.connect(lambda :self.msg(self.myButton1))
        layout.addWidget(self.myButton1)

        #提问对话框
        self.myButton2 = QPushButton(self)
        self.myButton2.setText("提问对话框")
        self.myButton2.clicked.connect(lambda: self.msg(self.myButton2))
        layout.addWidget(self.myButton2)

        # 警告对话框
        self.myButton3 = QPushButton(self)
        self.myButton3.setText("警告对话框")
        self.myButton3.clicked.connect(lambda: self.msg(self.myButton3))
        layout.addWidget(self.myButton3)

        # 严重错误对话框
        self.myButton4 = QPushButton(self)
        self.myButton4.setText("严重错误对话框")
        self.myButton4.clicked.connect(lambda: self.msg(self.myButton4))
        layout.addWidget(self.myButton4)

        # 关于对话框
        self.myButton5 = QPushButton(self)
        self.myButton5.setText("关于对话框")
        self.myButton5.clicked.connect(lambda: self.msg(self.myButton5))
        layout.addWidget(self.myButton5)

        self.setLayout(layout)


    def msg(self,btn):
        if btn.text()=="消息对话框":
            #使用infromation信息框
            reply=QMessageBox.information(self,'消息对话框','这是一个消息对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif btn.text()=="提问对话框":
            #使用question信息框
            reply=QMessageBox.question(self,'提问对话框','这是一个提问对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif btn.text()=="警告对话框":
            #使用warning信息框
            reply=QMessageBox.warning(self,'警告对话框','这是一个警告对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        elif btn.text()=="严重错误对话框":
            #使用critical信息框
            reply=QMessageBox.information(self,'严重错误对话框','这是一个严重错误对话框',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        else:
            #使用about信息框
            reply=QMessageBox.information(self,'关于对话框','这是一个关于对话框')

        print(reply)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MyWindow()
    form.show()
    sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class fileDialogDemo(QWidget):
    def __init__(self,parent=None):
        super(fileDialogDemo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        layout=QVBoxLayout()
        self.btn=QPushButton("加载图片")
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)

        #这下面三行就是用来后面放图片的
        self.le=QLabel("")
        self.le.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.le)

        self.btn1=QPushButton("加载文本文件")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)

        self.contents=QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)


    def getfile(self):
        fname,_=QFileDialog.getOpenFileName(self,'Open file',"../","Image files(*.jpg *.gif)")
        self.le.setPixmap(QPixmap(fname))

    def getfiles(self):
        dig=QFileDialog()
        dig.setFileMode(QFileDialog.AnyFile)
        dig.setFilter(QDir.Files)

        #下面这部分代码不是很熟悉，不太了解怎么回事，只知道是把文件中的东西拿出来放在self.content里面
        if dig.exec_():
            filenames=dig.selectedFiles()
            f=open(filenames[0],'r')

            with f:
                data=f.read()
                self.contents.setText(data)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=fileDialogDemo()
    form.show()
    sys.exit(app.exec_())



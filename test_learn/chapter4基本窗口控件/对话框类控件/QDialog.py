# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class DialogDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DialogDemo,self).__init__(parent)

        self.setWindowTitle("Dialog例子")
        self.resize(500,500)
        self.move(200,200)

        self.btn=QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50,50)
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog=QDialog()
        btn=QPushButton("ok",dialog)
        btn.move(50,50)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=DialogDemo()
    form.show()
    sys.exit(app.exec_())



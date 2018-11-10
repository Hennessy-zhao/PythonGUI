# -*- coding:UTF-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class ComboDemo(QWidget):
    def __init__(self,parent=None):
        super(ComboDemo,self).__init__(parent)

        self.setWindowTitle("QComboBox下拉列表框例子")
        self.resize(500,500)
        self.move(200,200)

        layout=QVBoxLayout()
        self.lpl=QLabel("")

        self.cb=QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItem("Python")
        self.cb.addItems(["PHP","java","ruby"])

        self.cb.currentIndexChanged.connect(self.selectIconchange)

        layout.addWidget(self.cb)
        layout.addWidget(self.lpl)
        self.setLayout(layout)

    def selectIconchange(self,i):
        self.lpl.setText(self.cb.currentText())
        print("Items in the list are:")
        for count in range(self.cb.count()):
            print('item'+str(count)+"="+self.cb.itemText(count))
            print("Current index",i,"selection changed",self.cb.currentText())



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=ComboDemo()
    form.show()
    sys.exit(app.exec_())
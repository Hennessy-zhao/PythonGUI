# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class spinDemo(QWidget):
    def __init__(self,parent=None):
        super(spinDemo,self).__init__(parent)

        self.setWindowTitle("QSpinBox计数器")
        self.resize(500,500)
        self.move(200,200)

        layout=QVBoxLayout()

        self.l1=QLabel("current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.sp=QSpinBox()
        self.sp.valueChanged.connect(self.valuechange)
        self.sp.setRange(-50,50)        #设置范围
        self.sp.setSingleStep(2)        #设置步长
        layout.addWidget(self.sp)

        self.setLayout(layout)

    def valuechange(self):
        self.l1.setText("current value: "+str(self.sp.value()))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=spinDemo()
    form.show()
    sys.exit(app.exec_())



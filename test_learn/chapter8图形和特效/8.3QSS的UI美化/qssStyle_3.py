# -*- coding:UTF-8 -*-
'''
QSS子控件
'''
from PyQt5.QtWidgets import *
import sys

class WindowDemo(QWidget):
    def __init__(self,parent=None):
        super(WindowDemo,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QComboBox样式")
        self.resize(500,500)
        self.move(200,200)

        combo=QComboBox(self)
        combo.setObjectName('myQComboBox')
        combo.addItem('Window')
        combo.addItem('Ubuntu')
        combo.addItem('Red Hat')

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WindowDemo()
    #定义QComboBox控件的QSS样式
    qssStyle='''
        QComboBox#myQComboBox::drop-down{
            image:url(../img/dropdown.png)
        }
    '''
    form.setStyleSheet(qssStyle)
    form.show()
    sys.exit(app.exec_())



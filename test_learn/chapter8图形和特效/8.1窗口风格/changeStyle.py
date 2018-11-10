# -*- coding:UTF-8 -*-
'''
设置窗口的风格
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys

class AppWidget(QWidget):
    def __init__(self,parent=None):
        super(AppWidget,self).__init__(parent)
        self.setGeometry(200,200,500,500)

        horizontalLayout=QHBoxLayout()
        self.styleLabel=QLabel("Set Style:")
        self.styleComboBox=QComboBox()
        #从QStyleFactory中增加多个显示样式
        self.styleComboBox.addItems(QStyleFactory.keys())
        #选择当前窗口风格
        index=self.styleComboBox.findText(
            QApplication.style().objectName(),
            QtCore.Qt.MatchFixedString
        )
        #设置当前窗口风格
        self.styleComboBox.setCurrentIndex(index)
        #通过comboBox控件选择窗口风格
        self.styleComboBox.activated[str].connect(self.handleStyleChanged)
        horizontalLayout.addWidget(self.styleLabel)
        horizontalLayout.addWidget(self.styleComboBox)
        self.setLayout(horizontalLayout)

    #改变窗口风格
    def handleStyleChanged(self,style):
        QApplication.setStyle(style)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=AppWidget()
    form.show()
    sys.exit(app.exec_())
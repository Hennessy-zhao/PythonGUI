# -*- coding:UTF-8 -*-
#在表格中快速定位到指定行

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
import sys

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget例子--快速定位到指定行")
        self.resize(600,800)
        self.move(200,200)

        conLayout=QHBoxLayout()
        tableWidget=QTableWidget(30,4)

        conLayout.addWidget(tableWidget)

        for i in range(30):
            for j in range(4):
                itemContent='(%d,%d)'%(i,j)
                tableWidget.setItem(i,j,QTableWidgetItem(itemContent))

        self.setLayout(conLayout)

        #遍历表格查找对应项
        text = "(10,1)"
        items = tableWidget.findItems(text, QtCore.Qt.MatchExactly)
        #items=tableWidget.find()
        item = items[0]

        # 选中单元格
        item.setSelected(True)
        # 设置单元格背景颜色为红色
        item.setForeground(QBrush(QColor(255, 0, 0)))

        row = item.row()
        # 通过鼠标滚轮定位，快速定位到11行
        tableWidget.verticalScrollBar().setSliderPosition(row)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Table()
    form.show()
    sys.exit(app.exec_())



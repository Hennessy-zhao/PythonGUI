# -*- coding:UTF-8 -*-
#改变单元格中显示图片的大小
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Table_Picture(QWidget):
    def __init__(self,parent=None):
        super(Table_Picture,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("改变单元格中显示图片大小的例子")
        self.resize(1000,1000)
        self.move(200,200)

        conLayout=QHBoxLayout()

        table=QTableWidget()
        table.setColumnCount(3)
        table.setRowCount(5)

        table.setHorizontalHeaderLabels(['图片1','图片2','图片3'])

        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setIconSize(QSize(300,200))

        #让列宽和图片相同
        for i in range(3):
            table.setColumnWidth(i,300)

        #让行高和图片相同
        for i in range(5):
            table.setRowHeight(i,200)

        #模拟产生15条记录
        for k in range(15):
            i=k/3
            j=k%3
            item=QTableWidgetItem()
            #用户点击表格时，图片被选中
            item.setFlags(Qt.ItemIsEnabled)
            icon=QIcon(r'../img/bao%d.png'%k)
            item.setIcon(QIcon(icon))

            print('e/icons/%d.png i=%d j=%d'%(k,i,j))
            table.setItem(i,j,item)

        conLayout.addWidget(table)
        self.setLayout(conLayout)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Table_Picture()
    form.show()
    sys.exit(app.exec_())



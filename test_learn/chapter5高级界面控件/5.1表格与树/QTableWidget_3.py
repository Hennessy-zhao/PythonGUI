# -*- coding:UTF-8 -*-
#设置单元格
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table,self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)

        layout=QVBoxLayout()

        tableWidget=QTableWidget()
        tableWidget.setRowCount(10)
        tableWidget.setColumnCount(3)
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','年龄'])

        #设置单元格文本颜色
        newItem=QTableWidgetItem("张三")
        newItem.setForeground(QBrush(QColor(255,0,0)))
        tableWidget.setItem(0,0,newItem)

        #将字体加粗
        newItem=QTableWidgetItem("男")
        newItem.setFont(QFont("Times",12,QFont.Black))
        tableWidget.setItem(0,1,newItem)

        #设置该单元格右对齐并与底部对齐
        newItem=QTableWidgetItem("22")
        newItem.setTextAlignment(Qt.AlignRight|Qt.AlignBottom)
        tableWidget.setItem(0,2,newItem)

        #向表格中多加几组数据
        func=lambda func:func(tableWidget)
        func(self.addTables)

        #设置单元格的排序方式
        tableWidget.sortItems(2,QtCore.Qt.DescendingOrder)      #升序是DescendingOrder

        #合并单元格,将第四行第一列的单元格，改为占据3行1列
        tableWidget.setSpan(3,0,3,1)

        #设置单元格大小
        #将第一列单元格宽度设置为150，第一行单元格高度设置为120
        tableWidget.setColumnWidth(0,150)
        tableWidget.setRowHeight(0,120)

        #在表格中不显示分割线
        #tableWidget.setShowGrid(False)

        #为单元格添加图片
        newItem=QTableWidgetItem(QIcon("../img/bao1.png"),"背包")
        tableWidget.setItem(2,2,newItem)

        #获得单元格中的内容
        tableWidget.itemClicked.connect(self.getItem)

        layout.addWidget(tableWidget)
        self.setLayout(layout)


    #获取单元格的内容
    def getItem(self,item):
        print('你点击的内容=> '+item.text())



    #向表格中多加几组数据
    def addTables(self,tableWidget):
        newItem = QTableWidgetItem("李四")
        tableWidget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem("男")
        tableWidget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem("18")
        tableWidget.setItem(1, 2, newItem)
        newItem = QTableWidgetItem("王五")
        tableWidget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem("女")
        tableWidget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem("28")
        tableWidget.setItem(2, 2, newItem)
        newItem = QTableWidgetItem("杨二")
        tableWidget.setItem(3, 0, newItem)
        newItem = QTableWidgetItem("女")
        tableWidget.setItem(3, 1, newItem)
        newItem = QTableWidgetItem("20")
        tableWidget.setItem(3, 2, newItem)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Table()
    form.show()
    sys.exit(app.exec_())



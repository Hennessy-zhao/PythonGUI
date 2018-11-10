# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table,self).__init__(parent)

        self.setWindowTitle("QTableView表格视图控件的例子")
        self.resize(800,500)
        self.move(200,200)
        dlgLayout = QVBoxLayout()

        self.model=QStandardItemModel(4,4)
        self.model.setHorizontalHeaderLabels(['标题1','标题2','标题3','标题4'])
        self.model.setVerticalHeaderLabels(['竖标题1','竖标题2','竖标题3','竖标题4'])

        for row in range(4):
            for column in range(4):
                item=QStandardItem("row %s,column %s"%(row,column))
                self.model.setItem(row,column,item)

        self.tableView=QTableView()
        self.tableView.setModel(self.model)
        #表格填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        dlgLayout.addWidget(self.tableView)

        #向表格中添加数据按钮
        button1=QPushButton("添加信息")
        button1.clicked.connect(self.addTable)
        dlgLayout.addWidget(button1)

        #删除表格中数据
        button2=QPushButton("删除选中行")
        button2.clicked.connect(self.delTable)
        button2.setToolTip("点击删除会删除掉当前选中的这一行\n如果什么也不选，默认删除第一行")
        dlgLayout.addWidget(button2)

        self.setLayout(dlgLayout)

    #添加新数据操作
    def addTable(self):
        item,ok=QInputDialog.getText(self,"输入你想要添加的这一行的内容",'输入内容(以空格间隔)')
        list=item.split(" ")
        if ok:
            self.model.appendRow([QStandardItem(list[0]),QStandardItem(list[1]),QStandardItem(list[2]),QStandardItem(list[3])])

    #删除新数据操作
    def delTable(self):
        index=self.tableView.currentIndex()
        self.model.removeRow(index.row())


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Table()
    form.show()
    sys.exit(app.exec_())



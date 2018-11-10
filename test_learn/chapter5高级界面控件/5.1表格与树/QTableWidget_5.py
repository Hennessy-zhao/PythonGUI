# -*- coding:UTF-8 -*-
#支持右键菜单
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table,self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setWindowTitle("QTableWidget支持右键菜单的例子")
        self.resize(500,500)
        self.move(200,200)

        conLayout=QHBoxLayout()
        self.tableWidget=QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)
        conLayout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        newItem=QTableWidgetItem("张三")
        self.tableWidget.setItem(0,0,newItem)

        newItem=QTableWidgetItem("男")
        self.tableWidget.setItem(0,1,newItem)

        newItem=QTableWidgetItem("160")
        self.tableWidget.setItem(0,2,newItem)

        #表格中第二行记录
        newItem = QTableWidgetItem("李四")
        self.tableWidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem("女")
        self.tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem("170")
        self.tableWidget.setItem(1, 2, newItem)

        #允许右键产生菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        #将右键菜单绑定到槽函数generateMenu
        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

        self.setLayout(conLayout)

    def generateMenu(self,pos):
        row_num=-1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num=i.row()
        #表格中只有两条有效数据，所以只在前两行支持右键弹出菜单
        if row_num<2:
            menu=QMenu()
            item1=menu.addAction(u"选项一")
            item2=menu.addAction(u"选项二")
            item3=menu.addAction(u"选项三")
            action=menu.exec_(self.tableWidget.mapToGlobal(pos))
            if action==item1:
                print('您选择了选项一')
            elif action==item2:
                print('您选择了选项二')
            elif action==item3:
                print('您选择了选项三')
            else:
                return
            print('当前行文字内容是：',self.tableWidget.item(row_num,0).text(),self.tableWidget.item(row_num,1).text(),self.tableWidget.item(row_num,2).text())


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Table()
    form.show()
    sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
#基本用法

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys

class Table(QWidget):
    def __init__(self,parent=None):
        super(Table,self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.resize(500,500)
        self.move(200,200)

        conLayout=QVBoxLayout()

        #下面的三行也可以用tablewidget=QTableWidget(4,3) 表示设置了一个4行3列的表格
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重(kg)'])

        #tableWidget.setVerticalHeaderLabels()可以设置表格的垂直表头标签
        #以下代码含义为不设置垂直表头标签，表格为自适应的伸缩模式，根据窗口大小来改变网格大小
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    #不设置也是自动伸缩的

        #将表格设置为禁止编辑
        #tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        #设置表格整行选中
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        #将行和列的宽度、高度设置为与所显示内容的宽度、高度相匹配(下面两行和书上不一致，只有列匹配了长度没有匹配)
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        #表格头的显示与隐藏
        tableWidget.verticalHeader().setVisible(False)
        tableWidget.horizontalHeader().setVisible(False)




        #以下为向表格中添加数据
        newItem=QTableWidgetItem("Hennessy")
        tableWidget.setItem(0,0,newItem)

        # 单元格中放置控件
        comBox=QComboBox()
        comBox.addItem("男")
        comBox.addItem("女")
        comBox.setStyleSheet("QComboBox{margin:3px};")
        tableWidget.setCellWidget(0,1,comBox)

        #添加按钮控件
        searchBtn=QPushButton("修改")
        searchBtn.setDown(True)
        searchBtn.setStyleSheet("QPushButton{margin:3px};")
        tableWidget.setCellWidget(0,2,searchBtn)

        conLayout.addWidget(tableWidget)

        # 在表格中快速定位到指定行
        btn=QPushButton("查找行")
        btn.clicked.connect(lambda:self.fondRow(tableWidget))
        conLayout.addWidget(btn)

        self.setLayout(conLayout)

    def fondRow(self,tableWidget):
        key, ok = QInputDialog.getText(self, "输入行数", '输入你要查找的内容')

        if tableWidget.findItems(key,QtCore.Qt.MatchExactly):
            items=tableWidget.findItems(key,QtCore.Qt.MatchExactly)
            item=items[0]

            #选中单元格
            item.setSelected(True)
            #设置单元格背景颜色为红色
            item.setForeground(QBrush(QColor(255,0,0)))

            row=item.row()
            #通过鼠标滚轮定位，快速定位到11行
            tableWidget.verticalScrollBar().setSliderPosition(row)
        else :
            QMessageBox.about(self,"错误","查找无效")

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Table()
    form.show()
    sys.exit(app.exec_())



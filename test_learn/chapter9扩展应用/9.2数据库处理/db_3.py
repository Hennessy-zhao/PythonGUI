# -*- coding:UTF-8 -*-
'''
使用QSqlTableModel，在窗口中使用该控件
setTable()设置要查询的表
setFilter()设置过滤器条件
select()查询
setEditStrategy()设置编辑策略
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
import sys

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
'''
在关闭窗口时断开数据连接
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sys

class ExecDatabaseDemo(QWidget):
    def __init__(self,parent=None):
        super(ExecDatabaseDemo,self).__init__(parent)

        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setDatabaseName("pyqttest")
        self.db.setUserName("root")
        self.db.setPassword("123456")
        self.db.open()

    def closeEvent(self, event):
        #关闭数据库
        self.db.close()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=ExecDatabaseDemo()
    form.show()
    sys.exit(app.exec_())
# -*- coding:UTF-8 -*-
'''
连接数据库，并且新建一个数据表，向数据表中添加数据
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

def createDB():
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setDatabaseName("pyqttest")
    db.setUserName("root")
    db.setPassword("123456")

    if not db.open():
        QMessageBox.critical(None,("无法打开数据库"),("无法建立到数据库的连接，这个例子需要QMYSQL支持，请检查数据库配置 \n\n单击取消按钮退出应用"),QMessageBox.Cancel)
        return False

    query=QSqlQuery()
    query.exec_("create table people(id int primary key,name varchar(20), address varchar(30))")
    query.exec_("insert into people values(1,'zhangsan1','BeiJing')")
    query.exec_("insert into people values(2,'lisi1','TianJin')")
    query.exec_("insert into people values(3,'wangwu1','HeNan')")
    query.exec_("insert into people values(4,'lisi1','HeBei')")
    query.exec_("insert into people values(5,'wangwu2','BShanghai')")
    #关闭数据库
    db.close()
    return True

if __name__ == '__main__':
    app=QApplication(sys.argv)
    createDB()
    sys.exit(app.exec_())

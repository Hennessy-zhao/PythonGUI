# -*- coding:UTF-8 -*-
'''
如何建立一个新的数据表，并且往数据表中添加数据
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
import sys

def createTableAndInit():
    #添加数据库
    db=QSqlDatabase.addDatabase("QMYSQL")
    #设置数据库名称
    db.setDatabaseName("pyqttest")
    db.setUserName("root")
    db.setPassword("123456")

    #判断是否打开数据库
    if not db.open():
        print(db.lastError().text())
        return False

    #声明数据库查询对象
    query=QSqlQuery()
    #创建表
    query.exec("create table student(id int primary key,name varchar(16),sex varchar(8),age int,deparent varchar(64))")

    #添加记录
    query.exec("insert into student values(1,'张三1','男',20,'计算机')")
    query.exec("insert into student values(2,'李四1','男',19,'经管')")
    query.exec("insert into student values(3,'王五1','男',22,'机械')")
    query.exec("insert into student values(4,'赵六1','男',21,'法律')")
    query.exec("insert into student values(5,'小明1','男',20,'英语')")
    query.exec("insert into student values(6,'小李1','女',19,'计算机')")
    query.exec("insert into student values(7,'小张1','男',20,'机械')")
    query.exec("insert into student values(8,'小刚1','男',19,'经管')")
    query.exec("insert into student values(9,'张三2','男',21,'计算机')")
    query.exec("insert into student values(10,'张三3','女',20,'法律')")

    db.close()
    return True

if __name__=='__main__':
    app=QApplication(sys.argv)
    createTableAndInit()
    sys.exit(app.exec_())



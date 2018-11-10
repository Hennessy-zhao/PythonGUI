'''
如何连接一个mysql数据库
'''
from PyQt5.QtSql import QSqlDatabase

db=QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost")
db.setDatabaseName("pyqttest")
db.setUserName("root")
db.setPassword("123456")

if db.open():
    print("1")
else :
    print(db.lastError().text())
db.close()
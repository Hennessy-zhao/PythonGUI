# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
import sys
import qdarkstyle

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)


        #每页几行数据
        self.messageNum=5
        self.initUI()


    def initUI(self):

        #创建窗口
        self.createWindow()

        # 创建表格
        self.createTable()

        #前一页按钮被按下
        self.preButton.clicked.connect(self.preButtonOnClick)

        #后一页按钮被按下
        self.nextButton.clicked.connect(self.nextButtonOnClick)

        #查找页按钮被按下
        self.jumpButton.clicked.connect(self.jumpButtonOnClick)

    def closeEvent(self, event):
        self.db.close()


    def createWindow(self):
        self.setWindowTitle("封装分页查询控件练习")
        self.resize(700,500)
        self.move(200,200)

        #设置页栏
        self.preButton=QPushButton("前一页")
        self.preButton.setStyleSheet('margin:0 20 0 20;')
        self.nextButton=QPushButton("后一页")
        self.nextButton.setStyleSheet('margin-right:20px')
        self.jumpleLabel=QLabel("跳转到第")
        self.jumplePage=QLineEdit()
        self.jumplePage.setFixedWidth(50)
        self.jumpButton=QPushButton("Go")
        self.jumpButton.setStyleSheet('margin-left:10;')

        self.pageLayout=QHBoxLayout()
        self.pageLayout.addWidget(self.preButton)
        self.pageLayout.addWidget(self.nextButton)
        self.pageLayout.addWidget(self.jumpleLabel)
        self.pageLayout.addWidget(self.jumplePage)
        self.pageLayout.addWidget(QLabel('页'))
        self.pageLayout.addWidget(self.jumpButton)
        self.pageLayout.addWidget(QSplitter())

        #设置表格栏，表格单元栏宽度自适应
        self.tableView=QTableView()
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #设置底部栏
        self.totalPage=QLabel()
        self.totalPage.setFixedWidth(20)
        self.currentPage=QLabel()
        self.currentPage.setFixedWidth(20)
        self.totalMessage=QLabel()
        self.totalMessage.setFixedWidth(20)
        self.bottomLayout=QHBoxLayout()
        self.bottomLayout.addWidget(QLabel("总共"))
        self.bottomLayout.addWidget(self.totalPage)
        self.ye = QLabel("页")
        self.ye.setStyleSheet('margin-right:50')
        self.bottomLayout.addWidget(self.ye)
        self.bottomLayout.addWidget(QLabel("当前第"))
        self.bottomLayout.addWidget(self.currentPage)
        self.bottomLayout.addWidget(QLabel('页'))
        self.bottomLayout.addWidget(QSplitter())
        self.bottomLayout.addWidget(QLabel("总共"))
        self.bottomLayout.addWidget(self.totalMessage)
        self.bottomLayout.addWidget(QLabel("条数据"))


        layout=QVBoxLayout()
        layout.addLayout(self.pageLayout)
        layout.addWidget(self.tableView)
        layout.addLayout(self.bottomLayout)
        self.setLayout(layout)


    #获取表格内容，分页显示
    def createTable(self):
        self.db=QSqlDatabase.addDatabase('QMYSQL')
        self.db.setDatabaseName('pyqttest')
        self.db.setUserName('root')
        self.db.setPassword('123456')

        #打开数据库
        self.db.open()
        #声明查询模型
        self.queryModel=QSqlQueryModel(self)

        #设置当前页数
        self.currentPageNum = 1
        #获取总页数
        self.totalPageNum=self.gettotalPageNum()
        # 获取总记录数
        self.totalMessageNum = self.getMessageNum()

        #刷新页面
        self.updateStatus()

        #设置总页数
        self.settotalPageNum()
        #设置总记录数
        self.settotalMessageNum()


        # 记录查询
        self.recordQuery(0)
        # 设置模型
        self.tableView.setModel(self.queryModel)



        #设置表格表头
        self.queryModel.setHeaderData(0,Qt.Horizontal,'编号')
        self.queryModel.setHeaderData(1,Qt.Horizontal,'姓名')
        self.queryModel.setHeaderData(2,Qt.Horizontal,'性别')
        self.queryModel.setHeaderData(3,Qt.Horizontal,'年龄')
        self.queryModel.setHeaderData(4,Qt.Horizontal,'院系')

    #记录查询
    def recordQuery(self,limitIndex):
        szQuery=("select * from student limit %d,%d"%(limitIndex,self.messageNum))
        self.queryModel.setQuery(szQuery)


    #获取总页数
    def gettotalPageNum(self):
        count=self.getMessageNum()
        if count%self.messageNum==0:
            num=count/self.messageNum
        else:
            num=count/self.messageNum+1
        return num

    #设置总页数
    def settotalPageNum(self):
        self.totalPage.setText(str(int(self.totalPageNum)))


    #获取总记录数
    def getMessageNum(self):
        self.queryModel.setQuery("select * from student")
        count=self.queryModel.rowCount()
        return count

    #设置总记录数
    def settotalMessageNum(self):
        self.totalMessage.setText(str(int(self.totalMessageNum)))

    #刷新页面
    def updateStatus(self):
        count=int(self.totalPageNum)

        if self.currentPageNum==count:
            self.preButton.setEnabled(True)
            self.nextButton.setEnabled(False)
        if self.currentPageNum==1:
            self.preButton.setEnabled(False)
            self.nextButton.setEnabled(True)

        self.currentPage.setText(str(int(self.currentPageNum)))
        self.jumplePage.setText('')

    #前一页按钮被按下
    def preButtonOnClick(self):
        page=self.currentPageNum
        page=int(page)
        limit=page-2
        self.currentPageNum=page-1
        self.recordQuery(limit)
        self.updateStatus()

    #后一页按钮被按下
    def nextButtonOnClick(self):
        page = self.currentPageNum
        page = int(page)
        self.currentPageNum = page + 1
        self.recordQuery(page)
        self.updateStatus()

    #查找页数按钮被按下
    def jumpButtonOnClick(self):
        page=self.jumplePage.text()

        count=int(self.totalPageNum)

        if not page.isdigit():
            QMessageBox.warning(self,'错误','抱歉，您输入的页码不是数字')
            return
        page = int(page)
        if page<1 or page >count:
            QMessageBox.warning(self,'错误','您输入的页码超出范围')
            return
        limitnum=(page-1)*self.messageNum
        self.currentPageNum=page
        self.recordQuery(limitnum)
        self.updateStatus()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    form.show()
    sys.exit(app.exec_())



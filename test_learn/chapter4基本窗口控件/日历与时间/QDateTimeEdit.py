# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo,self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDateTimeEdit例子")
        self.resize(500,500)
        self.move(200,200)

        vlayout=QVBoxLayout()

        self.dateEdit=QDateTimeEdit(QDateTime.currentDateTime(),self)

        self.dateEdit.setDisplayFormat("yyyy-MM-dd  HH:mm:ss")
        #设置最小日期
        #self.dateEdit.setMinimumDate(QDate(2000,1,1))      可以这样设置一个固定的日期，也可以:
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))

        #设置最大日期
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))

        #设置可以弹出日历控件
        self.dateEdit.setCalendarPopup(True)

        #设置槽函数，以下分别为：
        # 当日期发生变化时
        self.dateEdit.dateChanged.connect(self.onDateChanged)

        #无论是日期还是时间发生变化时执行
        self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged)

        #时间发生变化时执行
        self.dateEdit.timeChanged.connect(self.onTimeChanged)


        #设置按钮
        self.btn=QPushButton("获得日期和时间")
        self.btn.clicked.connect(self.onButtonClick)

        vlayout.addWidget(self.dateEdit)
        vlayout.addWidget(self.btn)
        self.setLayout(vlayout)


    #当日期发生变化时执行
    def onDateChanged(self,date):
        print(date)

    #当日期或时间或者二者一起发生变化时执行
    def onDateTimeChanged(self,datetime):
        print(datetime)

    #当时间发生变化时执行
    def onTimeChanged(self,time):
        print(time)

    #当按钮被按下去时执行
    def onButtonClick(self):
        dateTime=self.dateEdit.dateTime()

        #最大日期
        maxDate=self.dateEdit.maximumDate()

        #最小日期
        minDate=self.dateEdit.minimumDate()

        #最小日期时间
        minDateTime=self.dateEdit.minimumDateTime()

        #最小时间
        minTime=self.dateEdit.minimumTime()

        print('\n选择日期和时间')
        print("datetime=%s"%str(dateTime))
        print("maxDate=%s"%str(maxDate))
        print("minDate=%s"%minDate)
        print("minDateTime=%s"%minDateTime)
        print("minTime=%s"%minTime)







if __name__=='__main__':
    app=QApplication(sys.argv)
    form=DateTimeEditDemo()
    form.show()
    sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys

class CalendarExample(QWidget):
    def __init__(self,parent=None):
        super(CalendarExample,self).__init__(parent)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calendar例子")
        self.resize(500,500)
        self.move(200,200)

        self.cal=QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1980,1,1))
        self.cal.setMaximumDate(QDate(2020,1,1))
        #self.cal.setSelectedDate(QDate(2018,10,30))  设定一个被选定的日期，如果不设置默认为当日
        self.cal.setGridVisible(True)
        self.cal.move(20,20)
        self.cal.clicked[QtCore.QDate].connect(self.showDate)

        self.lb1=QLabel(self)
        date=self.cal.selectedDate()
        self.lb1.setText(date.toString("yyyy-MM-dd dddd"))
        self.lb1.move(20,300)

    def showDate(self,date):
        self.lb1.setText(date.toString("yyyy-MM-dd dddd"))



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=CalendarExample()
    form.show()
    sys.exit(app.exec_())



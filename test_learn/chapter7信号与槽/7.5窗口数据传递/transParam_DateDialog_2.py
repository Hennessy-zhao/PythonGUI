# -*- coding:UTF-8 -*-
'''
多窗口数据传递--信号与槽
该窗口为子窗口
子窗口发射的信号有两种，其中一种是发射PyQt内置的一些信号，另一种是发射自定义的信号
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from  PyQt5.QtGui import *

class DateDialog(QDialog):
    Signal_OneParameter=pyqtSignal(str)

    def __init__(self,parent=None):
        super(DateDialog,self).__init__(parent)
        self.setWindowTitle('子窗口：用来发射信号')

        #在布局中添加控件
        layout=QVBoxLayout(self)

        self.label1=QLabel(self)
        self.label1.setText('前者发射内置信号\n后者发射自定义信号')

        self.datetime_inner=QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        self.datetime_emit=QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.label1)
        layout.addWidget(self.datetime_inner)
        layout.addWidget(self.datetime_emit)

        #使用两个button(Ok和Cancel分别连接accept()和reject()槽函数)
        buttons=QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal,self
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.datetime_emit.dateTimeChanged.connect(self.emit_signal)

    def emit_signal(self):
        date_str=self.datetime_emit.dateTime().toString()
        self.Signal_OneParameter.emit(date_str)
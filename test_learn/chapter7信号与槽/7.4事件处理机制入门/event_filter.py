# -*- coding:UTF-8 -*-
'''
使用事件处理的方法－－３安装事件过滤器
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class EventFilter(QDialog):
    def __init__(self,parent=None):
        super(EventFilter,self).__init__(parent)
        self.setWindowTitle("事件过滤器")

        self.label1=QLabel("请点击")
        self.label2=QLabel("请点击")
        self.label3=QLabel("请点击")
        self.LabelState=QLabel('test')

        self.image1=QImage("../img/cartoon1.ico")
        self.image2=QImage("../img/cartoon2.ico")
        self.image3=QImage("../img/cartoon3.ico")

        self.width=600
        self.height=300

        self.resize(self.width,self.height)

        self.label1.installEventFilter(self)
        self.label2.installEventFilter(self)
        self.label3.installEventFilter(self)

        mainLayout=QGridLayout(self)
        mainLayout.addWidget(self.label1,500,0)
        mainLayout.addWidget(self.label2,500,1)
        mainLayout.addWidget(self.label3,500,2)
        mainLayout.addWidget(self.LabelState,600,1)
        self.setLayout(mainLayout)

    def eventFilter(self, watched,event):
        #只对label1的点击事件进行过滤，重写其行为，其他事件会被忽略
        if watched==self.label1:
            #对鼠标按下事件进行过滤，重写其行为
            if event.type()==QEvent.MouseButtonPress:
                mouseEvent=QMouseEvent(event)
                if mouseEvent.buttons()==Qt.LeftButton:
                    self.LabelState.setText("按下鼠标左键")
                elif mouseEvent.buttons()==Qt.MidButton:
                    self.LabelState.setText("按下鼠标中间键")
                elif mouseEvent.buttons()==Qt.RightButton:
                    self.LabelState.setText("按下鼠标右键")

                '''转换图片大小'''
                transform=QTransform()
                transform.scale(0.5,0.5)
                #令图片比原本大小小一半
                tmp=self.image1.transformed(transform)
                #将label1设置为有图标，并且图标大小是图片原本大小的一半
                self.label1.setPixmap(QPixmap.fromImage(tmp))
            #对鼠标释放事件进行过滤，重写其行为
            if event.type()==QEvent.MouseButtonRelease:
                self.LabelState.setText("释放鼠标按键")
                self.label1.setPixmap(QPixmap.fromImage(self.image1))


        #过滤一下label2被点击和释放
        if watched==self.label2:
            #对鼠标按下的行为进行过滤，重写其行为
            if event.type()==QEvent.MouseButtonPress:
                mouseEvent=QMouseEvent(event)
                if mouseEvent.buttons()==Qt.LeftButton:
                    self.LabelState.setText("按下鼠标左键")
                elif mouseEvent.buttons()==Qt.MidButton:
                    self.LabelState.setText("按下鼠标中间键")
                elif mouseEvent.buttons()==Qt.RightButton:
                    self.LabelState.setText("按下鼠标右键")

                '''转换图片大小'''
                transform1=QTransform()
                transform1.scale(2,2)
                #令图片比原来大一倍
                tmp2=self.image2.transformed(transform1)
                #将label2设置为有图标，并且图标大小是图片原本大小的一倍
                self.label2.setPixmap(QPixmap.fromImage(tmp2))
            #对鼠标释放事件进行过滤，重写其行为
            if event.type()==QEvent.MouseButtonRelease:
                self.LabelState.setText(("释放鼠标按键"))
                self.label2.setPixmap(QPixmap.fromImage(self.image2))

        # 对于其他情况，会返回系统默认的事件处理方法
        return QDialog.eventFilter(self,watched,event)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    form=EventFilter()
    form.show()
    sys.exit(app.exec_())
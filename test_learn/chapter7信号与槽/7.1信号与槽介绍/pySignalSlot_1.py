# -*- coding:UTF-8 -*-
'''
自定义信号与槽的使用
是指在发射信号时，不使用窗口控件的函数，而是使用自定义的函数
简单地说，就是使用pyqtSignal类实例发射信号
'''

from PyQt5.QtCore import *

#信号对象
class QTypeSignal(QObject):
    #定义一个信号
    sendmsg=pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal,self).__init__()

    def run(self):
        #发射信号
        self.sendmsg.emit('Hello PyQt5')

#槽对象
class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot,self).__init__()

    #槽对象中的槽函数
    def get(self,msg):
        print("QSlot get msg =>"+msg)

if __name__=='__main__':
    send=QTypeSignal()
    slot=QTypeSlot()

    #1
    print("---把信号绑定到槽函数上---")
    send.sendmsg.connect(slot.get)
    send.run()

    #2
    print("---把信号与槽函数的连接断开---")
    send.sendmsg.disconnect(slot.get)
    send.run()



# -*- coding:UTF-8 -*-
from PyQt5.QtCore import QObject,pyqtProperty
import sys

class MyObject(QObject):
    def __init__(self,intVal=20):
        self.val=intVal()

    def readVal(self):
        print('readVal=%s'%self.val)
        return self.val

    def setVal(self,val):
        print('setVal=%s'%val)
        self.val=val

    ppVal=pyqtProperty(int,readVal,setVal)





if __name__=='__main__':
    form=MyObject()
    form.show()




# -*- coding:UTF-8 -*-
'''
加载GIF动画效果
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class LoadingGifWin(QWidget):
    def __init__(self,parent=None):
        super(LoadingGifWin,self).__init__(parent)

        self.setWindowTitle("加载GIF动画效果")
        self.label=QLabel('',self)
        self.setFixedSize(128,128)
        self.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        self.movie=QMovie("../img/loading.gif")
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=LoadingGifWin()
    form.show()
    sys.exit(app.exec_())



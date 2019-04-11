# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Ui_plotly_pyqt_ui import Ui_MainWindow
from Plotly_PyQt5 import Plotly_PyQt5
import sys

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

        self.plotly_pyqt5=Plotly_PyQt5()
        self.qwebengine.setGeometry(QRect(50,20,1200,600))
        self.qwebengine.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_if_hs300_bais()))

        



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())
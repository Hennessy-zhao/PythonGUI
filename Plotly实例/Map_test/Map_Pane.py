# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Map_ui import Ui_MainWindow
from Map_Plotly import Plotly_PyQt5
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.plotly_pyqt5 = Plotly_PyQt5()
        self.widget.move(0,0)
        # self.widget.setGeometry(QRect(0, 0, 700, 700))
        self.widget.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
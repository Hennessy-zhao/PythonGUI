# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class ListViewDemo(QWidget):
    def __init__(self,parent=None):
        super(ListViewDemo,self).__init__(parent)

        self.setWindowTitle("QListView例子")
        self.resize(500,500)
        self.move(200,200)
        layout=QVBoxLayout()

        listView=QListView()
        slm=QStringListModel()
        self.qList=['Item1','Item2','Item3','Item4']
        slm.setStringList(self.qList)
        listView.setModel(slm)
        listView.clicked.connect(self.onClickView)

        layout.addWidget(listView)
        self.setLayout(layout)

    def onClickView(self,qModelIndex):
        QMessageBox.information(self,"ListWidget","你选择了:"+self.qList[qModelIndex.row()])



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=ListViewDemo()
    form.show()
    sys.exit(app.exec_())



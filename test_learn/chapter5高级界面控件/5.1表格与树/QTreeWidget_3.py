# -*- coding:UTF-8 -*-
#树形控件被单击时触发的响应时间
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class TreeWidgetDemo(QMainWindow):
    def __init__(self,parent=None):
        super(TreeWidgetDemo,self).__init__(parent)

        self.setWindowTitle("TreeWidget例子")
        self.resize(500,500)
        self.move(200,200)

        self.tree=QTreeWidget()
        #设置列数
        self.tree.setColumnCount(2)
        #设置树形控件头部的标题
        self.tree.setHeaderLabels(['Key','Value'])
        root=QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        root.setText(1,'0')

        child1=QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        child4 = QTreeWidgetItem(root)
        child4.setText(0, 'child4')
        child4.setText(1, '4')

        child5 = QTreeWidgetItem(root)
        child5.setText(0, 'child5')
        child5.setText(1, '5')

        self.tree.addTopLevelItem(root)
        self.tree.clicked.connect(self.onTreeClicked)

        self.setCentralWidget(self.tree)

    def onTreeClicked(self):
        item=self.tree.currentItem()
        QMessageBox.about(self,"显示结果","key=%s,value=%s"%(item.text(0),item.text(1)))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=TreeWidgetDemo()
    form.show()
    sys.exit(app.exec_())



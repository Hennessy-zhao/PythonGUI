# -*- coding:UTF-8 -*-
#树形结构的实现1
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class TreeWidgetDemo(QMainWindow):
    def __init__(self,parent=None):
        super(TreeWidgetDemo,self).__init__(parent)

        self.setWindowTitle("Demo")
        self.resize(500,500)
        self.move(200,200)


        self.tree=QTreeWidget()
        #设置列数
        self.tree.setColumnCount(2)
        #设置树形控件头部的标题
        self.tree.setHeaderLabels(['key','value'])
        #设置根节点
        root= QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        root.setIcon(0,QIcon("../img/root.png"))
        #设置树形控件的列的宽度
        self.tree.setColumnWidth(0,160)

        #设置子节点1
        child1=QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'ios')
        child1.setIcon(0,QIcon('../img/IOS.png'))

        #设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, ' ')
        child2.setIcon(0, QIcon('../img/android.png'))

        #设置子节点3
        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child3.setText(1, 'android')
        child3.setIcon(0, QIcon('../img/music.png'))

        self.tree.addTopLevelItem(root)

        #节点全部展开
        self.tree.expandAll()
        self.setCentralWidget(self.tree)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=TreeWidgetDemo()
    form.show()
    sys.exit(app.exec_())



# -*- coding:UTF-8 -*-
#树形结构的实现2
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
        #设置列
        self.tree.setColumnCount(2)
        #设置树形控件头部标题
        self.tree.setHeaderLabels(['Key','Value'])
        self.tree.setColumnWidth(0,260)

        #设置根节点
        root=QTreeWidgetItem()
        root.setText(0,'root')
        root.setIcon(0,QIcon('../img/root.png'))
        #设置节点的背景颜色
        brush_red=QBrush(Qt.red)
        root.setBackground(0,brush_red)
        brush_green=QBrush(Qt.green)
        root.setBackground(1,brush_green)

        rootList=[]
        rootList.append(root)

        #设置树形控件的子节点1
        child1=QTreeWidgetItem()
        child1.setText(0,'child')
        child1.setText(1,'ios')
        child1.setIcon(0,QIcon('../img/IOS.png'))
        #设置节点状态
        child1.setCheckState(0,Qt.Checked)
        root.addChild(child1)

        # 设置子节点2
        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, ' ')
        child2.setIcon(0, QIcon('../img/android.png'))

        # 设置子节点3
        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child3.setText(1, 'android')
        child3.setIcon(0, QIcon('../img/music.png'))

        self.tree.insertTopLevelItems(0,rootList)
        #节点全部展开
        self.tree.expandAll()


        self.setCentralWidget(self.tree)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=TreeWidgetDemo()
    form.show()
    sys.exit(app.exec_())



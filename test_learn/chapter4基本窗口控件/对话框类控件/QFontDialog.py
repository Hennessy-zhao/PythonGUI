# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class FontDialogDemo(QWidget):
    def __init__(self,parent=None):
        super(FontDialogDemo,self).__init__(parent)

        self.setWindowTitle("Font Dialog例子")
        self.resize(500,500)
        self.move(200,200)

        layout=QVBoxLayout()
        self.fontButton=QPushButton("choose font")
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)

        self.fontLineEdit=QLabel("Hello 测试字体例子")
        layout.addWidget(self.fontLineEdit)

        self.setLayout(layout)

    def getFont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(font)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=FontDialogDemo()
    form.show()
    sys.exit(app.exec_())



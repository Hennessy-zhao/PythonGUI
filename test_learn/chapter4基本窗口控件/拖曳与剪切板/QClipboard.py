# -*- coding:UTF-8 -*-
#剪切板的使用
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)

        self.setWindowTitle("QClipboard例子")
        self.resize(500,500)
        self.move(200,200)

        textCopyButton=QPushButton("&Copy Text")
        textPasteButton=QPushButton("Paste &Text")
        htmlCopyButton=QPushButton("C&opy HTML")
        htmlPasteButton=QPushButton("Paste &HTML")
        imageCopyButton=QPushButton("Co&py Image")
        imagePasteButton=QPushButton("Paste &Image")

        self.textLabel1=QLabel("")
        self.imageLabel1=QLabel()
        self.imageLabel1.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__),"../img/close.ico")))
        #上面一行写成self.imageLabel1.setPixmap(QPixmap("../img/close.ico"))也有相同的效果

        layout=QGridLayout()
        layout.addWidget(textCopyButton,0,0)
        layout.addWidget(imageCopyButton,0,1)
        layout.addWidget(htmlCopyButton,0,2)
        layout.addWidget(textPasteButton,1,0)
        layout.addWidget(imagePasteButton,1,1)
        layout.addWidget(htmlPasteButton,1,2)
        layout.addWidget(self.textLabel1,2,0,1,2)
        layout.addWidget(self.imageLabel1,2,2)
        self.setLayout(layout)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

    def copyText(self):
        clipboard=QApplication.clipboard()
        clipboard.setText("I'v been clipped")

    def pasteText(self):
        clipboard=QApplication.clipboard()
        self.textLabel1.setText(clipboard.text())

    def copyImage(self):
        clipboard=QApplication.clipboard()
        clipboard.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__),"../img/python.png")))

    def pasteImage(self):
        clipboard=QApplication.clipboard()
        self.imageLabel1.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        mimeData=QMimeData()
        mimeData.setHtml("<b>Bold and <font color=red>Red</font></b>")
        clipboard=QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard=QApplication.clipboard()
        mimeData=clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel1.setText(mimeData.html())




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Form()
    form.show()
    sys.exit(app.exec_())



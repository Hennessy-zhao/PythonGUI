# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QFormLayout
import sys

class lineEditDemo(QWidget):

    def __init__(self,parent=None):

        super(lineEditDemo,self).__init__(parent)
        self.setWindowTitle("QLineEdit例子")

        flo=QFormLayout()
        pNormalLineEdit=QLineEdit()
        pNoEchoLineEdit=QLineEdit()
        pPasswordLineEdit=QLineEdit()
        pPasswordEchoOnEditLineEdit=QLineEdit()

        flo.addRow("Normal",pNormalLineEdit)
        flo.addRow("NoEcho",pNoEchoLineEdit)
        flo.addRow("Password",pPasswordLineEdit)
        flo.addRow("PasswordEchoOnEdit",pPasswordEchoOnEditLineEdit)

        #文本框的浮显文字，即文本框提示信息placeholder
        pNormalLineEdit.setPlaceholderText("Normal")
        pNoEchoLineEdit.setPlaceholderText("NoEcho")
        pPasswordLineEdit.setPlaceholderText("Password")
        pPasswordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        #设置显示效果
        #正常显示字符
        pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        #不显示输入的字符
        pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        #显示密码掩饰字符
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        #输入时显示字符，不输入时显示密码掩饰字符
        pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(flo)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=lineEditDemo()
    form.show()
    sys.exit(app.exec_())
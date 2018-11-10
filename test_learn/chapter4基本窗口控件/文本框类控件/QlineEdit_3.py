# -*- coding:UTF-8 -*-

from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QFormLayout
import sys

class lineEditDemo(QWidget):

    def __init__(self,parent=None):
        super(lineEditDemo,self).__init__(parent)
        self.setWindowTitle("QLineEdit的输入掩码例子")

        flo=QFormLayout()
        pIPLineEdit=QLineEdit()
        pMACLineEdit=QLineEdit()
        pDataLineEdit=QLineEdit()
        pLicenseLineEdit=QLineEdit()

        pIPLineEdit.setInputMask("000.000.000.000;_")
        pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        pDataLineEdit.setInputMask("0000-00-00")
        pLicenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        flo.addRow("数字掩码",pIPLineEdit)
        flo.addRow("MAC掩码",pMACLineEdit)
        flo.addRow("日期掩码",pDataLineEdit)
        flo.addRow("许可证掩码",pLicenseLineEdit)

        self.setLayout(flo)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=lineEditDemo()
    form.show()
    sys.exit(app.exec_())
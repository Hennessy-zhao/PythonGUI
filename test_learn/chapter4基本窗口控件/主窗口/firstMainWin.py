import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.resize(300,300)
        self.status=self.statusBar()
        self.status.showMessage("这是状态栏提示",5000)     #这句话只出现10秒
        self.setWindowTitle("PyQt MainWindow例子")

if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon("./img/cartoon1.ico"))
    form=MainWindow()
    form.show()
    sys.exit(app.exec_())
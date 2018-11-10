#面向对象的写法
from PyQt5.QtWidgets import QMainWindow, QApplication,QPushButton
import sys

class WinForm(QMainWindow):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)

        self.setWindowTitle("屏幕坐标系统显示")
        btn=QPushButton(self)
        btn.setText("Button")

        btn.move(20,20)

        self.resize(500,500)

        self.move(100,100)

        print("QWidget:")
        print("w.x()=%d"%self.x())
        print("w.y()=%d"%self.y())
        print("w.width()=%d"%self.width())
        print("w.height()=%d"%self.height())
        print("QWidget.geometry:")
        print("widget.geometry().x()=%d"%self.geometry().x())
        print("widget.geometry().y()=%d"%self.geometry().y())
        print("widget.geometry().width()=%d"%self.geometry().width())
        print("widget.geometry().height()=%d"%self.geometry().height())

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())
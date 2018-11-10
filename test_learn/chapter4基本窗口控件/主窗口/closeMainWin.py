from PyQt5.QtWidgets import QMainWindow,QHBoxLayout,QPushButton,QApplication,QWidget,QDesktopWidget
import sys

class WinForm(QMainWindow):
    def __init__(self,parent=None):
        super(WinForm,self).__init__(parent)
        self.setWindowTitle('关闭窗口的例子')
        self.resize(500,500)

        #接下来三句话是把屏幕放在中间的意思
        screen=QDesktopWidget().screenGeometry()    #定义scren为了后面获取屏幕的长和宽
        size=self.geometry()    #获取该窗口本身的长和宽
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)    #把窗口移动到屏幕的正中间

        self.button1=QPushButton('关闭主窗口')        #定义一个按钮
        self.button1.clicked.connect(self.onButtonClick)    #当按钮被点击的时候触发onButtonClick

        layout=QHBoxLayout()
        layout.addWidget(self.button1)   


        main_frame=QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)
    def onButtonClick(self):
        # sender是发送信号的对象
        sender=self.sender()
        print(sender.text()+'被按下了')
        qApp=QApplication.instance()
        qApp.quit()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=WinForm()
    form.show()
    sys.exit(app.exec_())
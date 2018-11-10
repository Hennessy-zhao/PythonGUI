#屏幕坐标系统显示(面向对象写法见widgetGeometry_1.py)
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

app=QApplication(sys.argv)
widget=QWidget()
btn=QPushButton(widget)
btn.setText("Button")

#以QWidget左上角为(0,0)点
btn.move(20,20)

widget.resize(300,300)

#以屏幕左上角为(0,0)点
widget.move(200,200)


widget.setWindowTitle("PyQt坐标系统例子")
widget.show()

print("QWidget:")
print("w.x()=%d"%widget.x())
print("w.y()=%d"%widget.y())
print("w.width()=%d"%widget.width())
print("w.height()=%d"%widget.height())
print("QWidget.geometry:")
print("widget.geometry().x()=%d"%widget.geometry().x())
print("widget.geometry().y()=%d"%widget.geometry().y())
print("widget.geometry().width()=%d"%widget.geometry().width())
print("widget.geometry().height()=%d"%widget.geometry().height())
sys.exit(app.exec_())
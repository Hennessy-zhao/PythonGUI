# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detect.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1272, 900)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(243, 245, 248);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 30)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setContentsMargins(-1, 5, 0, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.widget_5)
        self.label_15.setMinimumSize(QtCore.QSize(60, 60))
        self.label_15.setMaximumSize(QtCore.QSize(60, 60))
        self.label_15.setStyleSheet("border-image: url(:/main/images/logo.png);\n"
"")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("padding-left:10px;")
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_14 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 15)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.widget_6.setFont(font)
        self.widget_6.setStyleSheet("background-color: rgb(41, 121, 255);\n"
"color: rgb(255, 255, 255);")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout.setContentsMargins(20, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_6)
        self.label_4.setMaximumSize(QtCore.QSize(35, 35))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setStyleSheet("border-image: url(:/main/images/icon2.png);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 2, 1)
        self.label_13 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 7, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_6)
        self.label_5.setMaximumSize(QtCore.QSize(35, 35))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setStyleSheet("border-image: url(:/main/images/icon4.png);")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 2, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setMaximumSize(QtCore.QSize(35, 35))
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setStyleSheet("border-image: url(:/main/images/icon3.png);")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 2, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_6)
        self.label_9.setMaximumSize(QtCore.QSize(35, 35))
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setStyleSheet("border-image: url(:/main/images/icon6.png);")
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 5, 2, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setMaximumSize(QtCore.QSize(35, 35))
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setStyleSheet("border-image: url(:/main/images/icon5.png);")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 2, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setMaximumSize(QtCore.QSize(35, 35))
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("border-image: url(:/main/images/icon1.png);")
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 4, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 5)
        self.gridLayout.setColumnStretch(7, 2)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setContentsMargins(30, -1, 20, 10)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding:20px;\n"
"border-radius:5px;")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background: rgb(3, 169, 244);\n"
"    color: rgb(255, 255, 255);\n"
"    box-shadow: rgba(0, 0, 0, 0.26) 0px 3px 9px 0px;\n"
"    border-radius:2px;\n"
"    border:1px solid rgb(3,169,244);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: rgb(3, 143, 206);\n"
"    border:1px solid rgb(2,134,194);\n"
"\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background:grey;\n"
"    border:none;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 12)
        self.verticalLayout_3.setStretch(2, 3)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("padding-left:30px;")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.widget_7 = QtWidgets.QWidget(self.widget_4)
        self.widget_7.setStyleSheet("border:3px solid white;\n"
"border-radius:5px;\n"
"margin:20px;")
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scan_label = QtWidgets.QLabel(self.widget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scan_label.sizePolicy().hasHeightForWidth())
        self.scan_label.setSizePolicy(sizePolicy)
        self.scan_label.setMinimumSize(QtCore.QSize(450, 450))
        self.scan_label.setStyleSheet("border-image: url(:/main/images/1.png);")
        self.scan_label.setText("")
        self.scan_label.setAlignment(QtCore.Qt.AlignCenter)
        self.scan_label.setObjectName("scan_label")
        self.horizontalLayout_3.addWidget(self.scan_label)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setContentsMargins(35, -1, 35, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.start_scan_btn = QtWidgets.QPushButton(self.widget_8)
        self.start_scan_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.start_scan_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_scan_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgb(125, 200, 85);\n"
"    color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(109, 175, 74);\n"
"    color:white;\n"
"    border-radius:5px;\n"
"}\n"
"")
        self.start_scan_btn.setObjectName("start_scan_btn")
        self.horizontalLayout_4.addWidget(self.start_scan_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.stop_scan_btn = QtWidgets.QPushButton(self.widget_8)
        self.stop_scan_btn.setMinimumSize(QtCore.QSize(200, 50))
        self.stop_scan_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_scan_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgb(252, 206, 84);\n"
"    color:white;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(236, 192, 78);\n"
"    color:white;\n"
"    border-radius:5px;\n"
"}\n"
"")
        self.stop_scan_btn.setObjectName("stop_scan_btn")
        self.horizontalLayout_4.addWidget(self.stop_scan_btn)
        self.verticalLayout_4.addWidget(self.widget_8)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 14)
        self.horizontalLayout.addWidget(self.widget_4)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 6)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 6)

        self.retranslateUi(Form)
        self.start_scan_btn.clicked.connect(Form.start_scan)
        self.stop_scan_btn.clicked.connect(Form.stop_scan)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "欢迎使用国家特殊生物检测系统"))
        self.label_14.setText(_translate("Form", "管理员"))
        self.label_13.setText(_translate("Form", "姓名：赵益石"))
        self.label_12.setText(_translate("Form", "工号：201830310116"))
        self.label_2.setStyleSheet(_translate("Form", "border:1px solod black;"))
        self.label_2.setText(_translate("Form", "扫描结果："))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">目前未扫描到特殊生物...</p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "查看详情"))
        self.label_10.setText(_translate("Form", "设备正在扫描中......"))
        self.start_scan_btn.setText(_translate("Form", "开始"))
        self.stop_scan_btn.setText(_translate("Form", "结束"))

import resource_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QtCore.QSize(500, 500))
        Form.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setEnabled(True)
        self.widget.setStyleSheet("QWidget#widget{\n"
"    border:2px solid #7397D1;\n"
"    margin:40px;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(80, 60, 80, 90)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#000;")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(55,88,139)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.usernum_le = QtWidgets.QLineEdit(self.widget)
        self.usernum_le.setEnabled(True)
        self.usernum_le.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.usernum_le.setFont(font)
        self.usernum_le.setStyleSheet("border:1px solid #8b8b8b;")
        self.usernum_le.setClearButtonEnabled(True)
        self.usernum_le.setObjectName("usernum_le")
        self.verticalLayout.addWidget(self.usernum_le)
        self.password_le = QtWidgets.QLineEdit(self.widget)
        self.password_le.setEnabled(True)
        self.password_le.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.password_le.setFont(font)
        self.password_le.setStyleSheet("border:1px solid #8b8b8b;")
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.verticalLayout.addWidget(self.password_le)
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("QPushButton{\n"
"    background-color:#37588B;\n"
"    color:#ffffff;\n"
"    border:none;    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(119,119,119);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:rgb(46, 75, 118)\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color:grey\n"
"}\n"
"")
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        self.usernum_le.textChanged['QString'].connect(Form.enable_login_btn)
        self.password_le.textChanged['QString'].connect(Form.enable_login_btn)
        self.login_btn.clicked.connect(Form.check_login)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "国家特殊生物检测系统"))
        self.label_2.setText(_translate("Form", "国 家 特 殊 生 物 检 测 系 统"))
        self.label.setText(_translate("Form", "登  录"))
        self.usernum_le.setPlaceholderText(_translate("Form", "请输入工号"))
        self.password_le.setPlaceholderText(_translate("Form", "请输入密码"))
        self.login_btn.setText(_translate("Form", "登 录"))

import resource_rc

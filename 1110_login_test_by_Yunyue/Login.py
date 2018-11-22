# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(340, 500)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 340, 500))
        self.widget.setObjectName("widget")
        self.LBP_password = QtWidgets.QLabel(self.widget)
        self.LBP_password.setGeometry(QtCore.QRect(40, 236, 40, 43))
        self.LBP_password.setText("")
        self.LBP_password.setObjectName("LBP_password")
        self.LB_RSpassword = QtWidgets.QLabel(self.widget)
        self.LB_RSpassword.setGeometry(QtCore.QRect(253, 285, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setUnderline(True)
        self.LB_RSpassword.setFont(font)
        self.LB_RSpassword.setObjectName("LB_RSpassword")
        self.LB_logo = QtWidgets.QLabel(self.widget)
        self.LB_logo.setGeometry(QtCore.QRect(40, 40, 265, 111))
        self.LB_logo.setText("")
        self.LB_logo.setObjectName("LB_logo")
        self.PB_login = QtWidgets.QPushButton(self.widget)
        self.PB_login.setGeometry(QtCore.QRect(40, 312, 265, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.PB_login.setFont(font)
        self.PB_login.setObjectName("PB_login")
        self.LE_password = QtWidgets.QLineEdit(self.widget)
        self.LE_password.setGeometry(QtCore.QRect(80, 236, 225, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.LE_password.setFont(font)
        self.LE_password.setObjectName("LE_password")
        self.PB_close = QtWidgets.QPushButton(self.widget)
        self.PB_close.setGeometry(QtCore.QRect(315, 0, 25, 25))
        self.PB_close.setText("")
        self.PB_close.setObjectName("PB_close")
        self.LE_username = QtWidgets.QLineEdit(self.widget)
        self.LE_username.setGeometry(QtCore.QRect(80, 190, 225, 43))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.LE_username.setFont(font)
        self.LE_username.setObjectName("LE_username")
        self.LBP_username = QtWidgets.QLabel(self.widget)
        self.LBP_username.setGeometry(QtCore.QRect(40, 190, 40, 43))
        self.LBP_username.setText("")
        self.LBP_username.setObjectName("LBP_username")
        self.LB_note = QtWidgets.QLabel(self.widget)
        self.LB_note.setGeometry(QtCore.QRect(40, 285, 190, 15))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.LB_note.setFont(font)
        self.LB_note.setText("")
        self.LB_note.setObjectName("LB_note")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "login_Dialog"))
        self.LB_RSpassword.setText(_translate("Dialog", "重置密码"))
        self.PB_login.setText(_translate("Dialog", "登录"))


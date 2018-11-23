# coding=utf-8
"""
继承自登录的基础界面——my_login_ui.py
使用sqlite和数据库jarvis.sqlite3交互
"""

import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QLabel, QApplication
from PyQt5.QtCore import *
from Login import Ui_Dialog
import db_IF as DB

class LoginLogic(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginLogic, self).__init__(parent)

        """初始化函数"""
        self.setupUi(self)
        self.retranslateUi(self)

        """窗口初始化"""
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        """输入框初始化"""
        # 此处改变密码输入框LEpassword的属性，使其不现实密码
        self.LE_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LE_username.setTextMargins(40, 0, 0, 0)
        self.LE_username.setPlaceholderText("请输入用户名")
        self.LE_password.setPlaceholderText("请输入密码")

        """logo初始化"""
        PNG_logo = QtGui.QPixmap('./images/LOGO1.png')
        self.LB_logo.setPixmap(PNG_logo)
        self.LB_logo.setScaledContents(True)

        """icon初始化"""
        PNG_username = QtGui.QPixmap('./images/username1.png')
        PNG_password = QtGui.QPixmap('./images/password1.png')
        self.LBP_username.setPixmap(PNG_username)
        self.LBP_username.setScaledContents(True)
        self.LBP_password.setPixmap(PNG_password)
        self.LBP_password.setScaledContents(True)
        self.PB_close.setStyleSheet("QPushButton{background-image: url(./images/close.png)}")

        """信号槽初始化"""
        # qt的信号槽机制，连接按钮的点击事件和相应的方法
        self.PB_login.clicked.connect(lambda: self.sign_in())
        # 关闭按钮关闭当前对话框
        self.PB_close.clicked.connect(self.close)
        self.PB_tosignup.clicked.connect(lambda :self.signup())
        # 输入框有输入时，清空提示信息
        self.LE_username.textChanged.connect(lambda : self.empty_note())
        self.LE_password.textChanged.connect(lambda: self.empty_note())

    def empty_note(self):
        self.LB_note.setText("")

    def sign_in(self):
        """
        登陆方法
        :return:
        """
        user_name = self.LE_username.text()
        user_password = self.LE_password.text()
        if user_name == "" or user_password == "":
            self.LB_note.setText("请输入用户名和密码")
        else:
            password = DB.IsExistUser(user_name)
            if not password:
                self.LB_note.setText("此用户未注册")
            else:
                if DB.hash(user_password) == password:
                    self.LB_note.setText("登陆成功")
                    time.sleep(1)
                    self.open_main_window()
                    self.close()
                else:
                    self.LB_note.setText("密码不正确")

    def signup(self):
        """
        去往注册的界面
        :return:
        """
        from my_signup_py import SignupLogic
        sig = SignupLogic()
        sig.show()
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginLogic()
    """qss初始化"""
    f = open(r'E:/Users/lenovo/PycharmProjects/Jarvis/style_syy.qss', "r", encoding='utf-8')
    style = f.read()
    app.setStyleSheet(style)
    ui.show()
    sys.exit(app.exec_())

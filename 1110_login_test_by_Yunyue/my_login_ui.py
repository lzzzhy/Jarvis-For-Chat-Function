# coding=utf-8
"""
登录的基础UI界面
"""


import sys
from PyQt5 import QtWidgets


class LoginUi(QtWidgets.QDialog):
    """
    这个类用来实现基础的登录界面展示
    没有交互功能
    包括“用户名”、“密码”、“登录按钮”、“提示标签”
    """
    def __init__(self):
        super(LoginUi, self).__init__()
        self.LBtips=QtWidgets.QLabel() # 提示文本
        self.LBuser = QtWidgets.QLabel() # 标签
        self.LBpassword = QtWidgets.QLabel()
        self.LEuser = QtWidgets.QLineEdit() # 文本框
        self.LEpassword = QtWidgets.QLineEdit()
        self.PBsignin = QtWidgets.QPushButton() # 按钮

        self.HLtips=QtWidgets.QHBoxLayout()
        self.HLuser = QtWidgets.QHBoxLayout()
        self.HLpassword = QtWidgets.QHBoxLayout()
        self.HLbutton = QtWidgets.QHBoxLayout()
        self.VLall = QtWidgets.QVBoxLayout()

        self.HLtips.addWidget(self.LBtips)
        self.HLuser.addWidget(self.LBuser)
        self.HLuser.addWidget(self.LEuser)
        self.HLpassword.addWidget(self.LBpassword)
        self.HLpassword.addWidget(self.LEpassword)
        self.HLbutton.addWidget(self.PBsignin)
        self.VLall.addLayout(self.HLtips)
        self.VLall.addLayout(self.HLuser)
        self.VLall.addLayout(self.HLpassword)
        self.VLall.addLayout(self.HLbutton)

        self.setLayout(self.VLall)

        self.setWindowTitle("登陆界面")
        self.LBtips.setText("")
        self.LBuser.setText("用户名:")
        self.LBpassword.setText("  密码:")
        self.PBsignin.setText("登录")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginUi()
    ui.show()
    sys.exit(app.exec_())
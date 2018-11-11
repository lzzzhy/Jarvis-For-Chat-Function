# coding=utf-8
"""
我先试着写一个注册的基础界面
注册的时候用“用户名”、“手机”和“密码”
有“确认密码”
暂时没有验证码
"""

from PyQt5 import QtWidgets
import sys


class SignupUI(QtWidgets.QDialog):
    def __init__(self):
        super(SignupUI, self).__init__()
        self.LBtips=QtWidgets.QLabel() # 提示文本/标签
        self.LBuser = QtWidgets.QLabel() # 用户名/标签
        self.LBphone = QtWidgets.QLabel()  # 手机号/标签
        self.LBpassword = QtWidgets.QLabel() # 密码/标签
        self.LBrepassword = QtWidgets.QLabel()  # 确认密码/标签
        self.LEuser = QtWidgets.QLineEdit() # 用户名/文本框
        self.LEphone = QtWidgets.QLineEdit()  # 手机号/文本框
        self.LEpassword = QtWidgets.QLineEdit() # 密码/文本框
        self.LErepassword = QtWidgets.QLineEdit()  # 确认密码/文本框
        self.PBsignup = QtWidgets.QPushButton() # 按钮

        self.HLtips=QtWidgets.QHBoxLayout()
        self.HLuser = QtWidgets.QHBoxLayout()
        self.HLphone = QtWidgets.QHBoxLayout()
        self.HLpassword = QtWidgets.QHBoxLayout()
        self.HLrepassword = QtWidgets.QHBoxLayout()
        self.HLbutton = QtWidgets.QHBoxLayout()
        self.VLall = QtWidgets.QVBoxLayout()

        self.HLtips.addWidget(self.LBtips)
        self.HLuser.addWidget(self.LBuser)
        self.HLuser.addWidget(self.LEuser)
        self.HLphone.addWidget(self.LBphone)
        self.HLphone.addWidget(self.LEphone)
        self.HLpassword.addWidget(self.LBpassword)
        self.HLpassword.addWidget(self.LEpassword)
        self.HLrepassword.addWidget(self.LBrepassword)
        self.HLrepassword.addWidget(self.LErepassword)
        self.HLbutton.addWidget(self.PBsignup)
        self.VLall.addLayout(self.HLtips)
        self.VLall.addLayout(self.HLuser)
        self.VLall.addLayout(self.HLphone)
        self.VLall.addLayout(self.HLpassword)
        self.VLall.addLayout(self.HLrepassword)
        self.VLall.addLayout(self.HLbutton)

        self.setLayout(self.VLall)

        self.setWindowTitle("注册界面")
        self.LBtips.setText("")
        self.LBuser.setText("  用户名:")
        self.LBphone.setText("  手机号:")
        self.LBpassword.setText("    密码:")
        self.LBrepassword.setText("确认密码:")
        self.PBsignup.setText("注册")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = SignupUI()
    ui.show()
    sys.exit(app.exec_())
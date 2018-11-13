# coding=utf-8
"""
继承自登录的基础界面——my_login_ui.py
使用sqlite和数据库jarvis.sqlite3交互
"""


import sys
import sqlite3
import hashlib
import time
from PyQt5 import QtWidgets
from my_login_ui import LoginUi


class LoginLogic(LoginUi):
    '''

    '''

    def __init__(self):
        super(LoginLogic, self).__init__()
        self.conn = sqlite3.connect("jarvis.sqlite3")
        # 此处改变密码输入框LEpassword的属性，使其不现实密码
        self.LEpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        # qt的信号槽机制，连接按钮的点击事件和相应的方法
        self.PBsignin.clicked.connect(lambda: self.sign_in())

    @staticmethod
    def hash(src):
        """
        哈希md5加密方法
        :param src: 字符串str
        :return:加密后的32位md5码
        """
        src = (src + "请使用私钥加密").encode("utf-8")
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()

    def sign_in(self):
        """
        登陆方法
        :return:
        """
        c_sqlite = self.conn.cursor()
        user_name = self.LEuser.text()
        user_password = self.LEpassword.text()
        if user_name == "" or user_password == "":
            self.LBtips.setText("请输入用户名和密码")
        else:
            c_sqlite.execute("""SELECT password FROM user WHERE name = ?""", (user_name,))
            password = c_sqlite.fetchall()
            if not password:
                self.LBtips.setText("此用户未注册")
            else:
                if self.hash(user_password) == password[0][0]:
                    self.LBtips.setText("登陆成功")
                    time.sleep(1)
                    self.open_main_window()
                    self.close()
                else:
                    self.LBtips.setText("密码不正确")

    def open_main_window(self):
        """
        此处添加登录成功后打开的另一个窗口的程序
        :return:
        """
        # 下方注释的代码根据自己的情况更改
        # ui = Ui_Dialog()
        # ui.show()
        print("打开另一个窗口")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginLogic()
    ui.show()
    sys.exit(app.exec_())
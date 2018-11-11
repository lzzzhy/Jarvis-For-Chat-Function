from MySignupUI import SignupUI
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import sqlite3
import hashlib
import time


# 继承界面
class SignupLogic(SignupUI):
    def __init__(self):
        super(SignupLogic, self).__init__()
        self.conn = sqlite3.connect("jarvis.sqlite3")
        try:
            create_tb_cmd = '''
                CREATE TABLE IF NOT EXISTS USER
                (NAME varchar(14) PRIMARY KEY,
                PHONE varchar(11) NOT NULL,
                PASSWORD char(32) NOT NULL
                );
                '''
            self.conn.execute(create_tb_cmd)
        except :
            print("Create table failed")


        # 此处改变密码输入框lineEdit_password的属性，使其不显示密码
        self.LEpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LErepassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LEpassword.setPlaceholderText("密码不超过15位")
        self.LErepassword.setPlaceholderText("请再次输入密码")
        regx = QRegExp("^[\S|\s]{15}$")
        self.LEpassword.setValidator(QRegExpValidator(regx, self.LEpassword))
        self.LErepassword.setValidator(QRegExpValidator(regx, self.LErepassword))

        # qt的信号槽机制，连接按钮的点击事件和相应的方法
        self.PBsignup.clicked.connect(lambda: self.sign_up())

    @staticmethod
    def hash(src):
        """
        哈希md5加密方法
        :param src: 字符串str
        :return:
        """
        src = (src + "请使用私钥加密").encode("utf-8")
        m = hashlib.md5()
        m.update(src)
        return m.hexdigest()


    def sign_up(self):
        """
        注册方法
        :return:
        """
        c_sqlite = self.conn.cursor()
        user_name = self.LEuser.text()
        user_phone=self.LEphone.text()
        user_password = self.LEpassword.text()
        user_repassword = self.LErepassword.text()
        if user_name == "" or user_phone == ""or user_password == ""or user_repassword == "":
            self.LBtips.setText("请将下列信息填写完整")
        elif user_password != user_repassword:
            self.LBtips.setText("密码不一致")
            self.LErepassword.setText("")
        else:
            user_password = self.hash(user_password)
            c_sqlite.execute("""select * from user where name = ?""", (user_name,))
            if not c_sqlite.fetchone():
                try:
                    c_sqlite.execute("""INSERT INTO USER VALUES (?,?,?)""", (user_name ,user_phone,user_password))
                except:
                    print("error")
                self.LBtips.setText("注册成功")
                self.conn.commit()
            else:
                self.LBtips.setText("用户名重复")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = SignupLogic()
    ui.show()
    sys.exit(app.exec_())
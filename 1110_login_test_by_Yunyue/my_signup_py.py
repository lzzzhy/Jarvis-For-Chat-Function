# coding=utf-8
"""

"""


import sys
import sqlite3
import random
import http.client
import urllib
import hashlib
import datetime
import re
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from my_signup_ui import SignupUI


class SignupLogic(SignupUI):
    """

    """
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
        # 且通过正则限制输入的字符长度最多为15位
        self.LEpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LErepassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LEpassword.setPlaceholderText("密码不超过15位")
        self.LErepassword.setPlaceholderText("请再次输入密码")
        regx = QRegExp("^[\S|\s]{15}$")
        self.LEpassword.setValidator(QRegExpValidator(regx, self.LEpassword))
        self.LErepassword.setValidator(QRegExpValidator(regx, self.LErepassword))

        # qt的信号槽机制，连接按钮的点击事件和相应的方法
        self.PBsignup.clicked.connect(lambda: self.sign_up())
        self.PBsendvcode.clicked.connect(lambda : self.creat_vcode())


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
        user_vcode=self.LEsendvcode.text()

        if user_name == "" or user_phone == ""or user_password == ""or user_repassword == ""or user_vcode == "":
            self.LBtips.setText("请将下列信息填写完整")
        elif user_password != user_repassword:
            self.LBtips.setText("密码不一致")
            self.LErepassword.setText("")
        elif user_vcode != self.verifycode:
            self.LBtips.setText("验证码错误，请重新输入")
            self.LEsendvcode.setText("")
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


    def creat_vcode(self):
        """
        生成验证码
        调用send_industry_sms()发送信息
        :return:
        """
        chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        x = random.choice(chars), random.choice(chars), random.choice(chars), random.choice(chars), random.choice(
            chars), random.choice(chars)
        self.verifycode = "".join(x)
        # 获取用户的手机号
        tos = self.LEphone.text()
        # 构造短信内容，需事先在秒嘀科技审核通过该短信模板
        smsContent = '【Jarvis for Chat】登录验证码：' + self.verifycode + '，如非本人操作，请忽略此短信。'
        # 验证手机号正确性
        ret = re.match(r"^1[35678]\d{9}$", tos)
        if tos == "":
            self.LBtips.setText("请填写手机号")
        elif ret:
            self.send_industry_sms(tos,smsContent)
        else:
            self.LBtips.setText("请填写符合规范的手机号")


    def send_industry_sms(self,tos, smsContent):
        """
        发送信息
        使用秒嘀科技API实现
        :return:
        """
        # 秒嘀科技注册后的账户信息
        accountSid = '6ac4f4828fef413ebaf90e5bf9bff782'          # ACCOUNT SID
        acctKey = '46cc515148fa4bf29fb571ed27b8fa63'          # AUTH TOKEN

        # 定义地址，端口等
        serverHost = "api.miaodiyun.com"
        serverPort = 443
        industryUrl = "/20150822/industrySMS/sendSMS"

        # 格式化时间戳，并计算签名
        timeStamp = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        rawsig = accountSid + acctKey + timeStamp
        m = hashlib.md5()
        m.update(rawsig.encode("utf8"))
        sig = m.hexdigest()

        # 定义需要进行发送的数据表单
        params = urllib.parse.urlencode(
            {'accountSid': accountSid,
             'smsContent': smsContent,
             'to': tos,
             'timestamp': timeStamp,
             'sig': sig
             }
        )

        # 定义header
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
        # 与构建https连接
        conn = http.client.HTTPSConnection(serverHost, serverPort)
        # Post数据
        conn.request(method="POST", url=industryUrl, body=params, headers=headers)
        # 返回处理后的数据
        response = conn.getresponse()
        # 读取返回数据
        jsondata = response.read().decode('utf-8')

        # 打印完整的返回数据，测试使用 #
        # print(jsondata)

        # 关闭连接
        conn.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = SignupLogic()
    ui.show()
    sys.exit(app.exec_())
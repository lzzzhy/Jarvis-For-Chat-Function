# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#主窗口
from PyQt5.QtWidgets import QLabel


class R_signin_layout(QWidget):

    zhanghao_lable: QLabel
    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        super(R_signin_layout, self).__init__(parent)
        self.resize(250, 600)
        # 设置主窗体标签
        self.setWindowTitle("右侧登录弹窗")

        self.rp_verticalLayout = QVBoxLayout(self)
        #设置布局的与主界面的边距
        #self.rp_verticalLayout.setContentsMargins(20, 20, 0, 30)
        #设置控件之间的垂直距离
        self.rp_verticalLayout.setSpacing(5)

        self.zhanghao_lable=QLabel(self)
        self.zhanghao_lable.setText("账号")
        self.zhanghao_lable.setFixedSize(60,20)
        #self.rp_GridLayout.addWidget(self.zhanghao_lable,1, 1,alignment = 0)
        self.rp_verticalLayout.addWidget(self.zhanghao_lable)

        self.rp_verticalLayout.addStretch(1)
        self.login_prompt=QLabel(self)
        self.login_prompt.setText("登录Jarvis For Chat")
        #self.login_prompt.setFixedSize(150,40)
        self.rp_verticalLayout.addWidget(self.login_prompt,0,Qt.AlignCenter)

        self.rp_verticalLayout.addStretch(1)
        self.push_login=QPushButton(self)
        self.push_login.setText("立即登录")
        self.push_login.setFixedSize(130,40)
        self.rp_verticalLayout.addWidget(self.push_login,0,Qt.AlignCenter)

        self.rp_verticalLayout.addStretch(3)
        self.log_button=QPushButton(self)
        self.log_button.setText("log")
        self.log_button.setFixedSize(210,60)
        self.rp_verticalLayout.addWidget(self.log_button,0,Qt.AlignCenter)

    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = R_signin_layout()
    ex.close_signal.connect(ex.close)
    ex.show()
    sys.exit(App.exec_())
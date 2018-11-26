# -*- coding: utf-8 -*-

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#主窗口
class FirstWindow(QWidget):

    close_signal = pyqtSignal()
    def __init__(self, parent=None):
        super(FirstWindow, self).__init__(parent)
        self.resize(250, 600)
        # 设置主窗体标签
        self.setWindowTitle("主窗口")

        self.rp_GridLayout = QGridLayout(self)
        self.zhanghao_lable=QLabel(self)
        self.zhanghao_lable.setText("账号")
        #self.rp_GridLayout.addWidget(self.zhanghao_lable,1, 1,alignment = 0)
        self.rp_GridLayout.addWidget(self.zhanghao_lable, 0, 0, 2, 1)
        self.touxiang_button=QPushButton(self)
        self.touxiang_button.setText("头像")
        self.touxiang_button.resize(100,100)
        self.rp_GridLayout.addWidget(self.touxiang_button, 1, 1, 2, 2)
        self.usename_lable=QLabel(self)
        self.usename_lable.setText("用户名")
        self.usename_lable.resize(100,50)
        self.rp_GridLayout.addWidget(self.usename_lable, 1, 3, 2, 2)
        self.change_button=QPushButton(self)
        self.change_button.setText("修改密码")
        self.change_button.resize(100,50)
        self.rp_GridLayout.addWidget(self.change_button, 2, 2, 1, 1)
        self.exit_button=QPushButton(self)
        self.exit_button.setText("退出登录")
        self.exit_button.resize(100,50)
        self.rp_GridLayout.addWidget(self.exit_button, 3, 2, 1, 1)
        self.log_button=QPushButton(self)
        self.log_button.setText("log")
        self.log_button.resize(100,50)
        self.rp_GridLayout.addWidget(self.log_button, 4, 1, 6, 2)

    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = FirstWindow()
    ex.close_signal.connect(ex.close)
    ex.show()
    sys.exit(App.exec_())
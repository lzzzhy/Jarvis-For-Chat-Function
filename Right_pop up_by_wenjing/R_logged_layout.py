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

        #嵌套布局
        self.rp_QFormLayout = QFormLayout(self)
        self.rp_qvbox = QVBoxLayout(self)
        self.form_qwiget=QWidget(self)
        self.form_qwiget.setLayout(self.rp_QFormLayout)
        self.setLayout(self.rp_qvbox)
        self.rp_qvbox.addWidget(self.form_qwiget)

        #设置布局的与主界面的边距
        #self.rp_QFormLayout.setContentsMargins(0, 0, 0, 30)
        #设置控件之间的垂直距离
        self.rp_QFormLayout.setVerticalSpacing(40)

        self.zhanghao_lable=QLabel(self)
        self.zhanghao_lable.setText("账号")
        self.zhanghao_lable.setFixedSize(60,20)
        self.rp_QFormLayout.addRow(self.zhanghao_lable,None)

        self.touxiang_button=QPushButton(self)
        self.touxiang_button.setText("头像")
        self.touxiang_button.setFixedSize(70,70)
        self.usename_lable=QLabel(self)
        self.usename_lable.setText("用户名")
        self.usename_lable.setFixedSize(100,40)
        self.rp_QFormLayout.addRow(self.touxiang_button,self.usename_lable)

        self.zhanghao_lable=QLabel(self)
        self.change_button=QPushButton(self)
        self.change_button.setText("修改密码")
        self.change_button.setFixedSize(100,40)
        self.exit_button=QPushButton(self)
        self.exit_button.setText("退出登录")
        self.exit_button.setFixedSize(100,40)
        self.rp_QFormLayout.addRow(self.change_button,self.exit_button)

        self.rp_qvbox.addStretch(3)
        self.log_button=QPushButton(self)
        self.log_button.setText("log")
        self.log_button.setFixedSize(210,60)
        self.rp_qvbox.addWidget(self.log_button,0,Qt.AlignCenter)

    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = FirstWindow()
    ex.close_signal.connect(ex.close)
    ex.show()
    sys.exit(App.exec_())
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
        self.resize(800, 600)
        # 设置主窗体标签
        self.setWindowTitle("主窗口")
        self.button = QToolButton(self)
        self.button.setText("弹窗")

    def closeEvent(self, event):
        self.close_signal.emit()
        self.close()

#右侧弹窗
class R_Popup(QWidget):
    def __init__(self, parent=None):
        super(R_Popup, self).__init__(parent)
        # 隐藏任务栏|去掉边框|顶层显示
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.resize(200, 600)
        #设置背景色便于区分
        self.setStyleSheet("background: black")
        #控制与主窗口大小和位置的一致
        self.tmpHwnd = None
        # 启动定时器检测主窗口的位置和大小
        self.checkTimer = QTimer(self, timeout=self.checkWindow)
        self.checkTimer.start(10)  # 10毫秒比较流畅

    #控制弹窗与主窗口的相对位置和大小
    def checkWindow(self):
        if ex.isMinimized():#最小化时
            self.hide()
        if not ex.isVisible():#主窗口关闭时
            self.close()
        if not self.isVisible():
            return
        else:
            #固定弹窗与主界面的相对位置
            self.move(ex.geometry().x()+ex.geometry().width()-self.geometry().width(), ex.geometry().y())
            #固定弹窗与主界面的相对大小
            self.resize(200,ex.geometry().height())

    #控制弹窗的显示和隐藏
    def handle_click(self):
        if not self.isVisible():
            self.show()
        else:
            self.hide()

    def handle_close(self):
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = FirstWindow()
    s = R_Popup()
    ex.button.clicked.connect(s.handle_click)
    #ex.btn.clicked.connect(ex.hide)
    ex.close_signal.connect(ex.close)
    ex.show()
    sys.exit(App.exec_())
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
class RightWindow(QWidget):
    def __init__(self, parent=None):
        super(RightWindow, self).__init__(parent)
        # 隐藏任务栏|去掉边框|顶层显示
        self.setWindowFlags(Qt.Tool | Qt.X11BypassWindowManagerHint | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.resize(500, 600)
        self.setStyleSheet("background: black")
        #控制与主窗口大小和位置的一致
        self.tmpHwnd = None
        # 启动定时器检测主窗口的位置和大小
        self.checkTimer = QTimer(self, timeout=self.checkWindow)
        self.checkTimer.start(10)  # 10毫秒比较流畅

    #控制弹窗与主窗口的相对位置和大小
    def checkWindow(self):
        if ex.isMinimized():
            self.hide()
        if not ex.isVisible():
            self.close()
        if not self.isVisible():
            return
        else:
            #固定弹窗与主界面的相对位置
            #print(ex.geometry().x(),ex.geometry().y())
            self.move(ex.geometry().x()+ex.geometry().width()-self.geometry().width(), ex.geometry().y())
            #固定弹窗与主界面的相对大小
            #print(ex.geometry().width(),ex.geometry().height())
            self.resize(200,ex.geometry().height())

    #入场动画
    def doAnim(self):
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(100)
        self.animation.setStartValue(QRect(ex.geometry().x()+ex.geometry().width(), ex.geometry().y(), 0, ex.geometry().height()))
        self.animation.setEndValue(QRect(ex.geometry().x()+ex.geometry().width()-200, ex.geometry().y(), 200, ex.geometry().height()))
        self.animation.start()

    #退场动画
    def doAnim2(self):
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(300)
        self.animation.setEndValue(QRect(ex.geometry().x() + ex.geometry().width(), ex.geometry().y(), 0, ex.geometry().height()))
        self.animation.setStartValue(QRect(ex.geometry().x() + ex.geometry().width(), ex.geometry().y(), 0, ex.geometry().height()))
        self.animation.start()

    def handle_click(self):
        if not self.isVisible():
            self.show()
            #self.doAnim()
        else:
            #self.doAnim2()
            self.hide()

    def handle_close(self):
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = FirstWindow()
    s = RightWindow()
    ex.button.clicked.connect(s.handle_click)
    #ex.btn.clicked.connect(ex.hide)
    ex.close_signal.connect(ex.close)
    ex.show()
    sys.exit(App.exec_())
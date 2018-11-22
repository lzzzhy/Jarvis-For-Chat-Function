import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        # 设置窗口初始位置和大小
        self.setGeometry(10, 10, 1000, 600)
        # 设置窗口居中
        self.center()
        # 设置窗口标题
        self.setWindowTitle('Jarvis For Chat 主界面框架')
        # 创建列表窗口，添加条目
        self.leftlist = QListWidget()

        self.leftlist.resize(150, 450)  ##想设置大小？？？

        self.leftlist.insertItem(0, '热词分析')
        self.leftlist.insertItem(1, '关键词提醒')
        self.leftlist.insertItem(2, '群发助手')
        self.leftlist.insertItem(3, '单向好友检索')

        # 创建4个小控件
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()
        # 在QStackedWidget对象中填充了4个子控件
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)

        # 水平布局，添加部件到布局中
        HBox = QHBoxLayout()
        HBox.addWidget(self.leftlist)
        HBox.addWidget(self.stack)
        HBox.setStretchFactor(self.leftlist,3)
        HBox.setStretchFactor(self.stack,17)
        self.setLayout(HBox)

        self.leftlist.currentRowChanged.connect(self.display)

    def center(self):# 设置窗口居中
        self.qr = self.frameGeometry()
        self.cp = QDesktopWidget().availableGeometry().center()
        self.qr.moveCenter(self.cp)
        self.move(self.qr.topLeft())

    #热词分析
    def stack1UI(self):
        # 水平布局
        self.layout=QFormLayout()

        self.logo= QPixmap('E:/pyprogram/1120-界面切换的研究/image/LOGO.jpg')
        self.l1=QLabel(self)
        self.l1.setGeometry(0, 0, 150, 150)
        #lbl.setScaledContents (True)  # 让图片自适应label大小
        #self.l1.setStyleSheet("border: 2px solid blue")
        self.l1.setPixmap(self.logo)
        self.l2 = QLabel('请在右侧列表中选择你感兴趣的群组及时间段', self)
        self.l3 = QLabel('开启你的【热词分析】之旅~', self)
        self.layout.addWidget(self.l1)
        self.layout.addWidget(self.l2)
        self.layout.addWidget(self.l3)

        self.qunlist = QListWidget()

        self.layout.addWidget(self.qunlist)
        #lb2 = QLabel(self)
        #lb2.setGeometry(0, 250, 300, 200)
        #lb2.setPixmap(pix)
        #lb2.setStyleSheet("border: 2px solid red")
        #lb2.setScaledContents(True)

        # 在窗口w中，新建一个lable，名字叫做l1
        #self.l1=layout.addWidget(QLabel('x'))
        #self.logo = QPixmap('E:/pyprogram/1120-界面切换的研究/image/LOGO.jpg')
        # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        #self.l1.setPix(self.logo)

        # 在窗口w中，新建一个lable，名字叫做l2
        #self.l2 = layout.addWidget(QLabel(self))
        #self.file = open('E:/pyprogram/1120-界面切换的研究/文本/热词介绍P1.txt')
        #self.reci=self.file.read()
        #self.l2.setText(self.reci)

        # 调整l1和l2的位置
        #self.l1.move(100, 20)
        #self.l2.move(140, 120)

        self.stack1.setLayout(self.layout)

    #关键词提醒
    def stack2UI(self):
        # 水平布局
        layout = QHBoxLayout()
        # 添加控件到布局中
        layout.addWidget(QLabel('关键词鸭'))
        self.stack2.setLayout(layout)

    #群发助手
    def stack3UI(self):
        # 水平布局
        layout = QHBoxLayout()
        # 添加控件到布局中
        layout.addWidget(QLabel('群发助手鸭'))
        self.stack3.setLayout(layout)

    #单向好友检测
    def stack4UI(self):
        # 水平布局
        layout = QHBoxLayout()
        # 添加控件到布局中
        layout.addWidget(QPushButton('开始检测'))

        self.stack4.setLayout(layout)

    def display(self, i):
        # 设置当前可见的选项卡的索引
        self.stack.setCurrentIndex(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    sys.exit(app.exec_())

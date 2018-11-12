from PyQt5 import QtCore, QtWidgets, QtGui
import complex
import sys
import time

class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = complex.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        # 初次更新日期框的值
        self.update_date()
        # 将日历控件的选择事件绑定到update_date函数
        self.calendar_change()

        # 初次更新LCD的值
        self.update_lcd()
        # 将update_lcd绑定到刻度盘的改变事件上
        self.dial_change()

        self.progressbar_connect()

        self.font_change()

        MainWindow.show()
        sys.exit(app.exec_())

    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    def calendar_change(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    def update_lcd(self):
        self.ui.lcdNumber.display(self.ui.dial.value())

    def dial_change(self):
        self.ui.dial.valueChanged['int'].connect(self.update_lcd)

    def font_change(self):
        self.ui.fontComboBox.activated['QString'].connect(self.ui.label.setText)

    def start_progressbar(self):
        self.b_stop_progress = False
        self.progress_value = self.ui.progressBar.value()

        while (self.progress_value <= 101) and not (self.b_stop_progress):
            self.ui.progressBar.setValue(self.progress_value)
            self.progress_value += 1
            time.sleep(0.3)
            QtWidgets.QApplication.processEvents()

    def stop_progressbar(self):
        self.b_stop_progress = True

    def reset_progressbar(self):
        self.progress_value = 0
        self.ui.progressBar.reset()
        self.b_stop_progress = False

    def progressbar_connect(self):
        self.ui.radioButton.clicked.connect(self.start_progressbar)
        self.ui.radioButton_2.clicked.connect(self.stop_progressbar)
        self.ui.radioButton_3.clicked.connect(self.reset_progressbar)
        self.progress_value = 0
        self.b_stop_progress = False





if __name__ == '__main__':
    MainWindow()
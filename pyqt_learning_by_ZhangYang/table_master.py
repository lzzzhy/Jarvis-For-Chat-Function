import table
from PyQt5 import QtCore, QtWidgets, QtGui
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = table.Ui_MainWindow()
    ui.setupUi(mainwindow)

    ui.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("数据0"))
    ui.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("数据1"))

    mainwindow.show()
    sys.exit(app.exec_())
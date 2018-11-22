
import sys
#form PyQt5.QtCore import
import PyQt5.QtCore 
from PyQt5.QtWidgets import *
#QApplication.setStyleSheet()
class winBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("demo.py")
        self.statusBar().showMessage("2018")
        self.resize(800,600)

        menu = self.menuBar()
        file_menu = menu.addMenu("file")
        edit_menu = menu.addMenu("edit")

        newfile_action = QAction('new file',self)
        file_menu.addAction(newfile_action)
        newfile_action.setStatusTip('create a new file') 

        exit_action = QAction('exit',self)
        exit_action.setStatusTip("Click to exit program")
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+F4')
        edit_menu.addAction(exit_action)
        
    
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    win = winBox()
    win.show()
    
    style = open(r"D:\2018software\Jarvis-For-Chat\pyqt_learning_by_Wangquanjiong\QSS-refer.qss","r",encoding='utf-8')
    style_str = style.read()
    #style_str = style_str.decode('utf-8')
    app.setStyleSheet(style_str)

    sys.exit(app.exec_())

 
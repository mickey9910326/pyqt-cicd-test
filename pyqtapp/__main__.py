import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal

from pyqtapp.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_1.clicked.connect(self.func1)
        self.pushButton_2.clicked.connect(self.func2)

    def func1(self):
        self.textBrowser.append('btn1 clicked')

    def func2(self):
        self.textBrowser.append('btn2 clicked')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

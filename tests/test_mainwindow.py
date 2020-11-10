import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyqtapp.__main__ import MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtTest import QTest

def test_btn1():
    app = QtWidgets.QApplication([])
    ui = MainWindow()
    QTest.mouseClick(ui.pushButton_1, QtCore.Qt.LeftButton)

    assert ui.textBrowser.toPlainText() == "btn1 clicked"

    app.deleteLater()

def test_btn2():
    app = QtWidgets.QApplication([])
    ui = MainWindow()
    QTest.mouseClick(ui.pushButton_2, QtCore.Qt.LeftButton)

    assert ui.textBrowser.toPlainText() == "btn2 clicked"

    app.deleteLater()

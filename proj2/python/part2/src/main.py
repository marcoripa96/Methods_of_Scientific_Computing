#!/usr/bin/env python3
import os
import sys
from PySide2 import QtCore, QtWidgets, QtGui
from components.main_window import MainWindow

# Main script which launches the application
if __name__ == '__main__':

    app = QtWidgets.QApplication([])
    QtGui.QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), "./assets/font/OpenSans-Regular.ttf"))
    mainWindow = MainWindow()
    font = QtGui.QFont("Open Sans")
    font.setPointSize(14)
    mainWindow.setFont(font)
    mainWindow.setWindowTitle('MCS')
    mainWindow.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "./assets/logo.png")))

    mainWindow.resize(800, 600)
    mainWindow.show()
    sys.exit(app.exec_())

"""INDEX FILE"""
import sys
import os
import gui.MainWindow as W
#import plugin
import MainPlugin as MP
#import PyQt4 gui library
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication(sys.argv)
Q = QtGui.QMainWindow()
D = W.Ui_MainWindow()
D.setupUi(Q)
Q.show()
sys.exit(app.exec_())

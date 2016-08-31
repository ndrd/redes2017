#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

#from chat import *

class Login(QtGui.QMainWindow):
    def __init__(self, isLocal=False):
        QtGui.QMainWindow.__init__(self)
        self.isLocal = isLocal
        self.initUI()

    def initUI(self):
        self.label1 = QtGui.QLabel('Mi puerto:', self)
        self.label1.resize(350,35)
        self.label1.move(20,10)

        self.line = QtGui.QLineEdit(self)
        self.line.resize(350,35)
        self.line.move(20,40)

        self.label2 = QtGui.QLabel('Puerto contacto:', self)
        self.label2.resize(350,35)
        self.label2.move(20,75)

        self.line2 = QtGui.QLineEdit(self)
        self.line2.resize(350,35)
        self.line2.move(20,100)

        self.label3 = QtGui.QLabel('IP contacto:', self)
        self.label3.resize(350,35)
        self.label3.move(20,135)

        self.line3 = QtGui.QLineEdit(self)
        self.line3.resize(350,35)
        self.line3.move(20,165)

        self.start = QtGui.QPushButton("Iniciar", self)
        self.start.resize(350,45)
        self.start.move(20,225)
        self.connect(self.start, QtCore.SIGNAL('clicked()'), self.initChat)

        self.setGeometry(300,300,370,350)
        self.setFixedSize(385,320)
        self.setWindowTitle("Iniciar chat")
        self.setWindowIcon(QtGui.QIcon(""))

        if self.isLocal:
            self.line3.setEnabled(False)
            self.line3.setText('127.0.0.1')

        self.show()

    def initChat(self):
        # self.chat = Chat(local=True,
        #                  local_port=self.line.text(),
        #                  cont_ip=None,
        #                  cont_port=self.line2.text())
        self.close()



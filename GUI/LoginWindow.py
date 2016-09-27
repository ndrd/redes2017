#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from ChatWindow import *
from Constants import Constants
#from chat import *

class Login(QtGui.QMainWindow):
    def __init__(self, local=False):
        QtGui.QMainWindow.__init__(self)
        self.isLocal = local
        self.initUI()

    def initUI(self):
        self.label1 = QtGui.QLabel('Puerto directorio:', self)
        self.label1.resize(350,35)
        self.label1.move(20,10)

        self.my_port = QtGui.QLineEdit(self)
        self.my_port.resize(350,35)
        self.my_port.move(20,40)

        self.label3 = QtGui.QLabel('IP directorio:', self)
        self.label3.resize(350,35)
        self.label3.move(20,75)

        self.cnt_ip = QtGui.QLineEdit(self)
        self.cnt_ip.resize(350,35)
        self.cnt_ip.move(20,100)

        self.label4 = QtGui.QLabel('Nombre de usuario:', self)
        self.label4.resize(350,35)
        self.label4.move(20,135)

        self.username = QtGui.QLineEdit(self)
        self.username.resize(350,35)
        self.username.move(20,160)

        self.start = QtGui.QPushButton("Iniciar", self)
        self.start.resize(350,45)
        self.start.move(20,225)
        self.connect(self.start, QtCore.SIGNAL('clicked()'), self.initChat)

        self.setGeometry(300,300,370,350)
        self.setFixedSize(385,320)
        self.setWindowTitle("Iniciar chat")
        self.setWindowIcon(QtGui.QIcon(""))

        if self.isLocal:
            self.cnt_ip.setEnabled(False)
            self.cnt_ip.setText('127.0.0.1')
        else:
            self.my_port.setText(str(Constants.CHAT_PORT))

        self.show()

    def initChat(self):
        a = Chat(local=self.isLocal,
                server_port=self.my_port.text(),
                server_ip=self.cnt_ip.text(),
                username=self.username.text())
        self.setParent(a)
        self.close()



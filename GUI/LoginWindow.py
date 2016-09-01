#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from ChatWindow import *
from Constants import Constants
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

        self.my_port = QtGui.QLineEdit(self)
        self.my_port.resize(350,35)
        self.my_port.move(20,40)

        self.label2 = QtGui.QLabel('Puerto contacto:', self)
        self.label2.resize(350,35)
        self.label2.move(20,75)

        self.cnt_prt = QtGui.QLineEdit(self)
        self.cnt_prt.resize(350,35)
        self.cnt_prt.move(20,100)

        self.label3 = QtGui.QLabel('IP contacto:', self)
        self.label3.resize(350,35)
        self.label3.move(20,135)

        self.cnt_ip = QtGui.QLineEdit(self)
        self.cnt_ip.resize(350,35)
        self.cnt_ip.move(20,165)

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
            self.my_port.setText(Constants.CHAT_PORT)
            self.cnt_prt.setText(Constants.CHAT_PORT)

        self.show()

    def initChat(self):
        a = Chat(local=self.isLocal,local_port=self.my_port.text(),cont_ip=self.cnt_ip.text(),cont_port=self.cnt_prt.text())
        self.close()



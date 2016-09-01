#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

from Channel.Channel import *

class Chat(QtGui.QMainWindow):

    def __init__(self, local, local_port, cont_ip, cont_port):
        QtGui.QMainWindow.__init__(self)

        self.chat_log = ''
        self.local_ip = '127.0.0.1'
        self.contact_port = cont_port
        self.contact_ip = cont_ip
        self.local_port = local_port

        # initialize channel
        self.channel = Channel(self.local_ip,
                               self.local_port,
                               self.contact_ip,
                               self.contact_port,
                               self)

        # initialize interface
        self.initUI()

    def initUI(self):

        self.logs = QtGui.QTextBrowser(self)
        self.logs.setAcceptRichText(True)
        self.logs.resize(620,400)
        self.logs.move(10,10)

        self.box = QtGui.QLineEdit(self)
        self.box.resize(470,45)
        self.box.move(10,420)

        self.send = QtGui.QPushButton("Send", self)
        self.send.resize(70,45)
        self.send.move(480,420)
        self.connect(self.send, QtCore.SIGNAL("clicked()"), self.sendMsg)

        self.call = QtGui.QPushButton("Call", self)
        self.call.resize(70,45)
        self.call.move(550,420)
        self.connect(self.call, QtCore.SIGNAL("clicked()"), self.startCall)

        self.setGeometry(300,300,640,480)
        self.setFixedSize(640,480)
        self.setWindowTitle("Chat")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    def sendMsg(self):
        # send message
        msg = unicode(self.box.text())
        self.channel.api_client.send_msg(msg)

        self.update_history('Ich: ', msg)
        self.box.clear()

    def startCall(self):
        MESSAGE = "Conectando..."
        self.channel.start_call()
        #code = QtGui.QMessageBox.about(self, "Sobre o LabControle2", MESSAGE)
        msg = QtGui.QMessageBox(self)
        msg.setText('Llamada en curso...')
        msg.setStandardButtons( QMessageBox.Cancel)
        code = msg.exec_()
        print 'Statting call ' + code

    def update_history(self, header, message):
        # update chat history
        self.chat_log = '<b>' + header + '</b>'  + message
        self.logs.append(self.chat_log)

    def incoming_call(self):
        msg = QtGui.QMessageBox(self)
        msg.setText('Aceptar Llamada...')
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        code = msg.exec_()
        print 'Status aceptacion cliente', code

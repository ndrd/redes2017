#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore
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
        self.box = QtGui.QLineEdit(self)
        self.box.resize(540,45)
        self.box.move(10,420)

        self.historial = QtGui.QTextBrowser(self)
        self.historial.setAcceptRichText(True)
        self.historial.resize(620,400)
        self.historial.move(10,10)

        self.responder = QtGui.QPushButton("Send", self)
        self.responder.resize(70,45)
        self.responder.move(560,420)
        self.connect(self.responder, QtCore.SIGNAL("clicked()"), self.sendMsg)

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

    def update_history(self, header, message):
        # update chat history
        self.chat_log = '<b>' + header + '</b>'  + message
        self.historial.append(self.chat_log)

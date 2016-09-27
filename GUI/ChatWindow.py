#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import cv

from PyQt4 import QtGui, QtCore, QtWebKit
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QPoint, QTimer
from PyQt4.QtGui import QApplication, QImage, QPainter, QWidget

from Channel.Channel import *

class Chat(QtGui.QMainWindow):

    def __init__(self, local, server_port, server_ip, username):
        QtGui.QMainWindow.__init__(self)

        self.chat_log = ''
        self.local_ip = '127.0.0.1'
        self.contact_port = '5001'
        self.contact_ip = 'locahost'
        self.local_port = '5000'

        # initialize channel
        self.channel = Channel(self.local_ip,
                               self.local_port,
                               self.contact_ip,
                               self.contact_port
                               )

        # initialize interface
        self.initUI()

    def initUI(self):

        self.logs = QtGui.QTextBrowser(self)
        self.logs.setAcceptRichText(True)
        self.logs.resize(620,400)
        self.logs.move(10,10)

        self.box = QtGui.QLineEdit(self)
        self.box.resize(390,45)
        self.box.move(10,420)

        self.send = QtGui.QPushButton("Send", self)
        self.send.resize(70,45)
        self.send.move(400,420)

        self.connect(self.send, QtCore.SIGNAL("clicked()"), self.sendMsg)

        self.call = QtGui.QPushButton("Call", self)
        self.call.resize(70,45)
        self.call.move(480,420)
        self.connect(self.call, QtCore.SIGNAL("clicked()"), self.startCall)


        self.video = QtGui.QPushButton("Video", self)
        self.video.resize(70,45)
        self.video.move(550,420)
        self.connect(self.video, QtCore.SIGNAL("clicked()"), self.startVideoCall)

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

    def startVideoCall(self):
        MESSAGE = "enlanzando..."
        self.channel.start_video_call()
        #code = QtGui.QMessageBox.about(self, "Sobre o LabControle2", MESSAGE)
        video_widget = VideoWidget(this)
        video_widget.open()
        self.reproduce()

    def reproduce(self):
        while True:
            if len(self.frames) > 0:
                cv2.imshow('Servidor',self.frames.pop(0))
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
        cv2.destroyAllWindows()


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

class Capture():
    def __init__(self):
        self.capturing = False
        self.c = cv2.VideoCapture(0)

    def startCapture(self):
        print "pressed start"
        self.capturing = True
        cap = self.c
        while(self.capturing):
            ret, frame = cap.read()
            cv2.imshow("Capture", frame)
            cv2.waitKey(5)
        cv2.destroyAllWindows()

    def endCapture(self):
        print "pressed End"
        self.capturing = False
        # cv2.destroyAllWindows()

    def quitCapture(self):
        print "pressed Quit"
        cap = self.c
        cv2.destroyAllWindows()
        cap.release()
        QtCore.QCoreApplication.quit()

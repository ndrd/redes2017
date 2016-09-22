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
        self.box.resize(390,45)
        self.box.move(10,420)

        self.send = QtGui.QPushButton("Send", self)
        self.call.resize(70,45)
        self.call.move(400,420)

        self.connect(self.send, QtCore.SIGNAL("clicked()"), self.sendMsg)

        self.call = QtGui.QPushButton("Call", self)
        self.send.resize(70,45)
        self.send.move(480,420)
        self.connect(self.call, QtCore.SIGNAL("clicked()"), self.startCall)


        self.call = QtGui.QPushButton("Video", self)
        self.call.resize(70,45)
        self.call.move(550,420)
        self.connect(self.call, QtCore.SIGNAL("clicked()"), self.startVideoCall)

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
        #ventana de recepcion
        playVThread = threading.Thread(target=self.reproduce)
        playVThread.setDaemon(True)
        playVThread.start()
        #code = QtGui.QMessageBox.about(self, "Sobre o LabControle2", MESSAGE)
        video_widget = VideoWidget(this)
        video_widget.open()

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

class IplQImage(QImage):
    """
    http://matthewshotton.wordpress.com/2011/03/31/python-opencv-iplimage-to-pyqt-qimage/
    A class for converting iplimages to qimages
    """

    def __init__(self,iplimage):
        # Rough-n-ready but it works dammit
        alpha = cv.CreateMat(iplimage.height,iplimage.width, cv.CV_8UC1)
        cv.Rectangle(alpha, (0, 0), (iplimage.width,iplimage.height), cv.ScalarAll(255) ,-1)
        rgba = cv.CreateMat(iplimage.height, iplimage.width, cv.CV_8UC4)
        cv.Set(rgba, (1, 2, 3, 4))
        cv.MixChannels([iplimage, alpha],[rgba], [
        (0, 0), # rgba[0] -> bgr[2]
        (1, 1), # rgba[1] -> bgr[1]
        (2, 2), # rgba[2] -> bgr[0]
        (3, 3)  # rgba[3] -> alpha[0]
        ])
        self.__imagedata = rgba.tostring()
        super(IplQImage,self).__init__(self.__imagedata, iplimage.width, iplimage.height, QImage.Format_RGB32)


class VideoWidget(QWidget):
    """ A class for rendering video coming from OpenCV """

    def __init__(self, parent=None):
        QWidget.__init__(self)
        self._capture = cv.CreateCameraCapture(0)
        # Take one frame to query height
        frame = cv.QueryFrame(self._capture)
        self.setMinimumSize(frame.width, frame.height)
        self.setMaximumSize(self.minimumSize())
        self._frame = None
        self._image = self._build_image(frame)
        # Paint every 50 ms
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.queryFrame)
        self._timer.start(50)

    def _build_image(self, frame):
        if not self._frame:
            self._frame = cv.CreateImage((frame.width, frame.height), cv.IPL_DEPTH_8U, frame.nChannels)
        if frame.origin == cv.IPL_ORIGIN_TL:
            cv.Copy(frame, self._frame)
        else:
            cv.Flip(frame, self._frame, 0)
        return IplQImage(self._frame)

    def queryFrame(self):
        frame = cv.QueryFrame(self._capture)
        self._image = self._build_image(frame)
        self.update()




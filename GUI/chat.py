# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat.ui'
#
# Created: Sat Mar  7 19:32:20 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Chat(object):
    def __init__(self, Chat):
        Chat.setObjectName(_fromUtf8("Chat"))
        Chat.resize(855, 648)
        self.centralwidget = QtGui.QWidget(Chat)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 851, 631))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.webChat = QtWebKit.QWebView(self.verticalLayoutWidget)
        self.webChat.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webChat.setObjectName(_fromUtf8("webChat"))
        self.horizontalLayout_2.addWidget(self.webChat)
        self.lsContacts = QtGui.QListView(self.verticalLayoutWidget)
        self.lsContacts.setObjectName(_fromUtf8("lsContacts"))
        self.horizontalLayout_2.addWidget(self.lsContacts)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.slZoom = QtGui.QSlider(self.verticalLayoutWidget)
        self.slZoom.setMinimum(100)
        self.slZoom.setMaximum(500)
        self.slZoom.setOrientation(QtCore.Qt.Horizontal)
        self.slZoom.setInvertedAppearance(False)
        self.slZoom.setInvertedControls(False)
        self.slZoom.setTickPosition(QtGui.QSlider.NoTicks)
        self.slZoom.setTickInterval(1)
        self.slZoom.setObjectName(_fromUtf8("slZoom"))
        self.verticalLayout.addWidget(self.slZoom)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leMsg = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.leMsg.setEnabled(True)
        self.leMsg.setObjectName(_fromUtf8("leMsg"))
        self.horizontalLayout.addWidget(self.leMsg)
        self.btnSend = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.horizontalLayout.addWidget(self.btnSend)
        self.btnAuth = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btnAuth.setObjectName(_fromUtf8("btnAuth"))
        self.horizontalLayout.addWidget(self.btnAuth)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.leUrl = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.leUrl.setObjectName(_fromUtf8("leUrl"))
        self.verticalLayout.addWidget(self.leUrl)
        Chat.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chat)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "Chat", None))
        self.btnSend.setText(_translate("Chat", "Send", None))
        self.btnAuth.setText(_translate("Chat", "Auth", None))

from PyQt4 import QtWebKit

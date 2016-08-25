from login_g import *
from chat import *
from Channel import *
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

class DialogLogin(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_DialogLogin(self)
        self.ui.lineEdit_srv.setText("127.0.0.1")
        self.ui.lineEdit_srv_2.setText("")
        self.ui.lineEdit_srv_3.setText("")
        self.setup()

    def setLocalMode(self, mode):
        self.ui.lineEdit_srv.setDisabled(mode)


    def setup(self):
        QtCore.QObject.connect(self.ui.pushButton_log, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)

    def login(self):
        contact_ip = self.ui.lineEdit_srv.text()
        contact_port = self.ui.lineEdit_srv_2.text()
        user_port = self.ui.lineEdit_srv_3.text()
        if not contact_ip or not user_port or not contact_port:
            print('ERROR, debes especificar las direcciones')
        else:
            chat = Chat(contact_ip,user_port,msg)
            chat.show()

    def openRegDlg(self):
        regDlg = RegisterDialog()
        regDlg.exec_()
        regDlg.destroy()
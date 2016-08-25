from login_g import *
from chat_g import *
from Channel import *
from PyQt4 import QtCore, QtGui
from Constants import Constants
from Constants import AuxiliarFunctions

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

class ChatDialog(QtGui.QDialog):
    def __init__(self,local, user_port, contact_ip, contact_port,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_ChatDialog(self)

        if not local:
            self.user_ip = AuxiliarFunctions.get_ip_address()
            print(self.user_ip)




class DialogLogin(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_DialogLogin(self)
        self.ui.lineEdit_srv.setText(str(Constants.DEFUALT_HOST))
        self.ui.lineEdit_srv_2.setText(str(Constants.DEFAULT_USER_PORT))
        self.ui.lineEdit_srv_3.setText(str(Constants.DEFAULT_CONTACT_PORT))
        self.setup()
        self.isLocal = False
        self.isShowed = False

    def setLocalMode(self, mode):
        self.ui.lineEdit_srv.setDisabled(mode)
        self.isLocal = mode


    def setup(self):
        QtCore.QObject.connect(self.ui.pushButton_log, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)

    def login(self):
        contact_ip = self.ui.lineEdit_srv.text()
        contact_port = self.ui.lineEdit_srv_2.text()
        user_port = self.ui.lineEdit_srv_3.text()
        is_local =  self.isLocal 
        if not contact_ip or not user_port or not contact_port:
            print('ERROR, debes especificar las direcciones')
        else:
            if not self.isShowed:
                chat = ChatDialog(is_local, user_port, contact_ip, contact_port, self)
                chat.show()
                self.isShowed = True


    def openRegDlg(self):
        regDlg = RegisterDialog()
        regDlg.exec_()
        regDlg.destroy()
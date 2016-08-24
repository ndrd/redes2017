from login_gui import *

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

class LoginDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_LoginDialog(self)
        self.ui.lineEdit_srv.setText("127.0.0.1")
        self.ui.lineEdit_usr.setText("347473")
        self.ui.lineEdit_pas.setText("123456")
        self.setup()
    def setup(self):
        #self.ui.Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowSystemMenuHint)
        QtCore.QObject.connect(self.ui.pushButton_log, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)
        QtCore.QObject.connect(self.ui.pushButton_reg, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openRegDlg)
    def login(self):
        srv_ip = self.ui.lineEdit_srv.text()
        user_no = self.ui.lineEdit_usr.text()
        pwd = self.ui.lineEdit_pas.text()
        if not srv_ip or not user_no or not pwd:
            self.ui.label_error.setText(u"Enter a user or password")
            return
        self.ui.label_error.setText(u"Un momento...")
        msg = net.login(srv_ip, user_no, pwd)
        if not msg or msg=='LOGIN FAIL':
            msg = u"login failed"
            self.ui.label_error.setText(msg)
        else:
            self.accept()
            mainWin = MainWindow(srv_ip,user_no,msg)
            mainWin.show()
    def openRegDlg(self):
        regDlg = RegisterDialog()
        regDlg.exec_()
        regDlg.destroy()
from PyQt4 import QtCore, QtGui
from login import *
class LoginDialog(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_DialogLogin()
        self.setup()
    def setup(self):
        #self.ui.Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowSystemMenuHint)
        QtCore.QObject.connect(self.ui.pushButton_log, QtCore.SIGNAL(_fromUtf8("clicked()")), self.login)
    def login(self):
        srv_ip = self.ui.lineEdit_srv.text()
        user_no = self.ui.lineEdit_usr.text()
        pwd = self.ui.lineEdit_pas.text()
        if not srv_ip or not user_no or not pwd:
            self.ui.label_error.setText(u"Enter a user or password")
            return
        print "login..." 
        self.ui.label_error.setText(u"Entrando...")
        msg = net.login(srv_ip, user_no, pwd)
        if not msg or msg=='LOGIN FAIL':
            msg = u"login failed"
            self.ui.label_error.setText(msg)
        else:
            self.accept()
            mainWin = MainWindow(srv_ip,user_no,msg)
            mainWin.show()
    def openRegDlg(self):
        print "register..."
        regDlg = RegisterDialog()
        regDlg.exec_()
        regDlg.destroy()
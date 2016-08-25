#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

from Constants import AuxiliarFunctions
from SimpleXMLRPCServer import *

class MyApiServer(AuxiliarFunctions.MyThread):

    def __init__(self, my_ip, my_port, gui):
        super(MyApiServer, self).__init__()
        self.my_ip =  my_ip
        self.my_port =  my_port

        self.server = SimpleXMLRPCServer(
                        (my_ip, int(my_port)),
                        requestHandler=Handler,
                        allow_none=True)

        self.server.register_instance(FunctionWrapper(gui, self.server))
        self.server.register_instrospection_functions()

    def run(self):
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.server.server_close()
            sys.exit(0)



class FunctionWrapper:

    def __init__(self, gui, server):
        self.server =  server
        self.gui =  gui

    def sendMessage_wrapper(self, message):
        self.gui.update_history('\nyour friend says: ', message)



class Handler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',);



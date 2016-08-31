#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import SIGNAL

from SimpleXMLRPCServer import SimpleXMLRPCServer
from threading import Thread
from Constants import *

class MyApiServer(Thread):
    def __init__(self, my_ip, my_port, gui):
        super(MyApiServer, self).__init__()
        self.port = my_port if my_port else 5000
        self.server = SimpleXMLRPCServer(("localhost", int(self.port)), allow_none = True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.funtionWrapper = FunctionWrapper(gui)
        self.server.register_instance(self.funtionWrapper)
        self.gui = gui

    def run(self):
        print('Listening on port', self.port, '...')
        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received, exiting.")
            self.server.server_close()
            sys.exit(0)

class FunctionWrapper:
    """ **************************************************
    Constructor de la clase
    ************************************************** """
    def __init__(self, gui):
        self.gui =  gui
        print "Se construye las funciones"
   
    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        print "El:"+ message+"\n"
        self.gui.emit(QtCore.SIGNAL("agregarMensaje(QString)"), message)
        self.gui.update_history('Eso dijo:', message);
    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para regresar el texto
    ************************************************** """
    def echo(self, message):
        return message



#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ApiClient import *
from ApiServer import *

from Constants import Constants

"""**************************************************
Las instancias de esta clase contendran los metodos
necesarios para hacer uso de los metodos
del api de un contacto. Internamente Trabajara
con una proxy apuntando hacia los servicios del
servidor xmlrpc del contacto
**************************************************"""
class Channel:
	def __init__(self, user_ip, user_port,
				contact_ip, contact_port, gui):
		self.proxy = 'http://' + contact_ip + ':' +  contact_port
		self.user_ip = user_ip
		self.user_port = user_port
		self.api_server = MyApiServer(user_ip, user_port, gui)
		self.api_client = MyApiClient(str(self.proxy))
		print str(self.proxy)
		self.api_server.start()

	def send_text(self, txt):
		self.api_client.send_msg(txt)


#! /usr/bin/env python
# -*- coding: utf-8 -*-

from ApiClient import *
from ApiServer import *
from RecordAudio import *
from RecordVideo import *

import numpy
import multiprocessing as mp
import xmlrpclib

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
		self.api_server = MyApiServer(user_ip, user_port, Functions(gui))
		self.api_client = MyApiClient(str(self.proxy))
		self.queue = mp.Queue()
		self.video_queue = mp.Queue()
		self.recorder = Recorder(self.queue)
		self.video_recorder = VideoRecorder(self.video_queue)
		self.call_in_course = False
		self.call_process = None
		self.api_server.start()

	def send_text(self, txt):
		self.api_client.send_msg(txt)

	def stop_call(self):
		if self.recorder.is_alive():
			self.recorder.terminate()


	def start_call(self):
		self.recorder.start()
		while True:
		    d = self.queue.get()
		    data = xmlrpclib.Binary(d)
		    self.api_client.play_audio(data)

    def start_video_call(self):
    	self.video_recorder.start()
    	while True:
    	    d = self.video_queue.get()
    	    data = xmlrpclib.Binary(d)
    	    self.api_client.play_video(data)

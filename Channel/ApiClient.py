#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xmlrpclib
from Constants import *

class MyApiClient:

    def __init__(self, proxy_uri):
        if proxy_uri is not None:
            self.server = xmlrpclib.ServerProxy(proxy_uri,
                                                allow_none=True)

    def send_msg(self, message):
        print(self.server.sendMessage_wrapper(message))

    def play_audio(self, data):
    	print self.server.playAudio(data)

    def play_video(self, data):
        print self.server.playVideo(data)

    def request_incomming_call(self):
    	print (self.server.request_incoming_call())
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
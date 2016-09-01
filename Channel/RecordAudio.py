#! /usr/bin/env python


#####################################################
# PURPOSE:                                          #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes: installar pyaudio (python-pyaudio)         #
#        installar  jackd qjackctl                  #
#                                                   #
# Copyright   31-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

"""
Graba audio y manda el stream

"""

from threading import Thread
import time
import xmlrpclib

import pyaudio
import numpy

CHUNK = 1024
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2

class Recorder(Thread):
    def __init__(self, queue):
        super(Recorder, self).__init__()
        self.queue = queue

    def run(self):
        p = pyaudio.PyAudio()
        FORMAT = p.get_format_from_width(2)

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)    

        while True:
            frame = []
            for i in range(0,int(RATE/CHUNK * RECORD_SECONDS)):
                frame.append(stream.read(CHUNK))
            data_ar = numpy.fromstring(''.join(frame),  dtype=numpy.uint8)
            self.queue.put(data_ar)






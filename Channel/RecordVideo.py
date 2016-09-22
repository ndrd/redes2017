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
Graba audio y manda el stream de video

"""
import numpy as np
import cv
import multiprocessing as mp
import time
import xmlrpclib
import numpy
from cStringIO import StringIO
from numpy.lib import format

class VideoRecorder(Thread):
    def __init__(self, queue):
        super(Recorder, self).__init__()
        self.queue = queue
        self.cap = cv.VideoCapture(0)

    def toString(data):
        f = StringIO()
        format.write_array(f,data)
        return f.getvalue()

    def run(self):
        while(True):
            ret, frame = self.cap.read()
            cv2.imshow('Cliente',frame) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            data = xmlrpclib.Binary(toString(frame))
            self.queue.put(data)
        cap.release()
        cv2.destroyAllWindows()






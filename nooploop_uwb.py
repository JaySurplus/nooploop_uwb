#!/usr/bin/env python3


import threading
import serial
import json
from queue import Queue
from nooploop_uwb_helper import *

class Nooploop_UWB_AOA(object):
    """nooploop uwb aoa parser.
    """

    def __init__(self, config_path=None):
        """
        Input:
            config_path: str
        """
        def __searialthread():
            while self.serthread_alive:
                if self.serial.in_waiting:
                    data = self.serial.read(self.serial.in_waiting)
                    self.binbuffer.extend(data)
                else:
                    pass

                try:
                    while True:
                        header = find_frameheader(self.binbuffer)
                        print(self.binbuffer[header+32])
                except:
                    pass

        if config_path:
            with open(config_path) as f:
                self.config = json.load(f)
            
            port = self.config['port']
            baudrate = self.config['baudrate']
            role = self.config['role']

        
        self.serial = serial.Serial(port, baudrate, timeout=None)
        self.data_fifo = Queue()
        
        self.serthread_alive = True
        self.binbuffer = []

        self.serthread = threading.Thread(target=__searialthread)
        self.serthread.start()

    def get_data(self, timeout=None):
        data = self.data_fifo.get(block=True, timeout=timeout)
        return data

    def terminate(self):
        """Terminal UWB Instance
        """
        self.serthread_alive = False
        self.serial.close()
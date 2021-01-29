#!/usr/bin/env python3


import threading
import serial
import json
from queue import Queue
from nooploop_uwb.utils.nooploop_uwb_helper import *

class AOA(object):
    """nooploop uwb aoa parser.
    role:  1=Anchor, 2=Tag
    """
    def __init__(self, config_path=None, port='/dev/ttyUSB1', baudrate=9216000):
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
                        head_pos, tail_pos = get_one_complete_frame(self.binbuffer)
                        frame = self.binbuffer[head_pos:tail_pos]
                        self.binbuffer=self.binbuffer[tail_pos:]
                        self.data_fifo.put(frame)
                except:
                    pass

        if config_path:
            with open(config_path) as f:
                self.config = json.load(f)
            
            self.port = self.config['port']
            self.baudrate = self.config['baudrate']

        else:
            self.port = port
            self.baudrate = baudrate
        self.role = None
        self.id = None
        self.valid_node_quantity = None
        self.node = []        
        self.voltage = 0

        self.serial = serial.Serial(self.port, self.baudrate, timeout=None)
        self.data_fifo = Queue()
        
        self.serthread_alive = True
        self.binbuffer = []

        self.serthread = threading.Thread(target=__searialthread)
        self.serthread.start()

    def __str__(self):
        return self.get_data_json()


    def get_data(self, timeout=None):
        frame_data = self.data_fifo.get(block=True, timeout=timeout)


        self.role = frame_data[4]
        self.id = frame_data[5]
        self.valid_node_quantity = frame_data[20]
        self.voltage = (frame_data[18] | frame_data[19] << 8) / 1000
        self.node = []

        for i in range(self.valid_node_quantity):
            self.node.append(AOA_Anchor(frame_data[21+11*i: 32+11*i]).get_data())
        
        res_dic = {
            "role": self.role,
            "id": self.id,
            "voltage": self.voltage,
            "node_quantity": self.valid_node_quantity,
            "nodes": {i: self.node[i] for i in range(len(self.node))}
        }
        
        return res_dic

    def get_data_json(self):
        """Return all informations in json format for exchanging.
        Input:
            None
        Output:
            res_json: json string.
        """
        data_dic = self.get_data()
        data_json = json.dumps(data_dic, indent=4)
        return data_json



    def terminate(self):
        """Terminal UWB Instance
        """
        self.serthread_alive = False
        self.serial.close()




class AOA_Anchor(object):
    def __init__(self, data):


        def __signed_int(v, bits=16):
            if v & (1<<(bits-1)):
                v -= 1<<bits
            return v
        self.role = data[0]
        self.id = data[1]
        self.dist = (data[2] << 8 | data[3] << 16 | data[4] << 24) / 256000
        self.angle =  __signed_int(data[5] | (data[6]<<8)) / 100
        self.fp_rssi = data[7] / -2
        self.rx_rssi = data[8] / -2

    def get_role(self):
        return self.role
    
    def get_id(self):
        return self.id
    
    def get_dist(self):
        return self.dist

    def get_angle(self):
        return self.angle
    
    def get_fp_rssi(self):
        return self.fp_rssi
    
    def get_rx_rssi(self):
        return self.rx_rssi
    
    def __str__(self):
        s = "role: {:>6}\nid: {:>6}\ndistance: {:>6}\nangle: {:>6}\nfp_rssi: {:>6}\nrx_rssi: {:>6}".format(self.get_role(),self.get_id(), self.get_dist(),self.get_angle(), self.get_fp_rssi(), self.get_rx_rssi())
        return s
    
    def get_data(self):
        """Return all infomations in dictionary format.
        Input:
            None
        Output:
            res_dic: dict
        """
        res_dic = {
            "role": self.get_role(),
            "id": self.get_id(),
            "distance": self.get_dist(),
            "angle": self.get_angle(),
            "fp_rssi": self.get_fp_rssi(),
            "rx_rssi": self.get_rx_rssi()
        }
        return res_dic

    def get_json(self):
        """Return all informations in json format for exchanging.
        Input:
            None
        Output:
            res_json: json string.
        """
        res_dic = self.get_data()
        res_json = json.dumps(res_dic, indent=4) 
        return res_json
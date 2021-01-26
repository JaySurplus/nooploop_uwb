import threading
import struct
import datetime


class NooploopUWB_Frame_Exception(Exception):
    def __init__(self, err='AOA Frame Error'):
        Exception.__init__(self, err)

class NooploopUWB_Frame_Invalid_Exception(Exception):
    def __init__(self, err='No Valid Frame Exception'):
        Exception.__init__(self, err)

class NooploopUWB_Frame_Incomplete_Exception(Exception):
    def __init__(self, err='No Complete Frame Exception'):
        Exception.__init__(self, err)

class NooploopUWB_Frame_Error_Exception(Exception):
    def __init__(self, err='Error Frame'):
        Exception.__init__(self, err)



def find_frameheader(buffer_list:list):
    while True:
        try:
            header_index = buffer_list.index(0x55)
        except ValueError:
            raise NooploopUWB_Frame_Incomplete_Exception

        if header_index + 1 == len(buffer_list):
            raise NooploopUWB_Frame_Incomplete_Exception

        if buffer_list[header_index+1] == 0x07:
            return header_index
        
        else:
            buffer_list = buffer_list[header_index+1:]
import threading
import struct
import datetime
from queue import Queue

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



def __parse_frame_length(buffer_list:list, head_pos):
    high = buffer_list[head_pos+3]
    low = buffer_list[head_pos+2]
    
    combine = (high << 8) + low
    return combine 

def __parse_node_quantity(buffer_list:list, head_pos):
    return buffer_list[head_pos+20]

def __verify_length(buffer_list:list, head_pos, frame_length):
    node_quantity = __parse_node_quantity(buffer_list, head_pos)

    base_length = 22
    
    if frame_length != base_length + 11 * node_quantity:
        raise NooploopUWB_Frame_Incomplete_Exception

    if head_pos + frame_length > len(buffer_list):
        #print(head_pos + frame_length , len(buffer_list))
        raise NooploopUWB_Frame_Incomplete_Exception

def __verify_frame_crc(buffer_list:list, head_pos, tail_pos):
    """Verify CRC of a parsed frame
    Input:
        buffer_list: list
        head_pos: head position index of a frame
        tail_pos: tail position index of a frame
    Output:
        None
    Exception:
        NooploopUWB_Frame_Error_Exception
    """

    frame = buffer_list[head_pos:tail_pos]

    calculated_crc = sum(frame[:-1])
    crc = frame[-1]
    mask = 0x00ff
    if (calculated_crc&mask) != crc:
        raise NooploopUWB_Frame_Error_Exception


def find_frameheader(buffer_list:list):
    """Find frame header. Header start with 0x55, then follow by 0x07

    Input:  
        buffer_list: list
    Output:
        header_index: int
    Exception:
        NooploopUWB_Frame_Incomplete_Exception

    """
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


def get_one_complete_frame(buffer_list:list):
    """Get head position and tail position of a valid frame.
    Input:
        buffer_list: list
    Output:
        head_pos: int
        tail_pos: int
    """
    head_pos = find_frameheader(buffer_list)
    frame_length = __parse_frame_length(buffer_list, head_pos)

    __verify_length(buffer_list, head_pos, frame_length)

    tail_pos = head_pos + frame_length

    __verify_frame_crc(buffer_list, head_pos, tail_pos)
    
    return head_pos, tail_pos



def get_information_from_valid_frame(buffer_list:list, data_fifo:Queue):
    """Extract information from a valid frame.
    Input:
        buffer_list: list, buffer contains frame.
        data_fifo: Queue, Send valid information to queue.
    """
    pass
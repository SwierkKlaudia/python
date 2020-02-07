from board_driver_simulator import open,close,but,pot,det,led,set_port,get_port
from my_board import set_point,get_key,step,get_detector,wait_for_key,get_pot

import time

try:
    open()
#---------------------


    while(True):
        get_pot()

    
            
#---------------------
finally:
    close()

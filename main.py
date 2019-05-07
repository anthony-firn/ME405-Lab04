# -*- coding: utf-8 -*-
#
## @privatesection - Stuff in this file doesn't need to be Doxygen-ed
#
#  @author jr

import pyb
import micropython
import gc

import cotask
import task_share
import print_task

import controller
import encoder
import motor
import time
import utime

# Allocate memory so that exceptions raised in interrupt service routines can
# generate useful diagnostic printouts
micropython.alloc_emergency_exception_buf (100)

pinC0 = pyb.Pin (pyb.Pin.board.PC0, pyb.Pin.ANALOG)
queue = task_share.Queue('f', 1000)
adc = pyb.ADC(pinC0)
pinC1 = pyb.Pin (pyb.Pin.board.PC1, pyb.Pin.OUT_PP)

def main():
    global pinC0 
    global queue
    global adc
    global pinC1
    tim = pyb.Timer(1)   
    tim.init(freq= 1000)
    tim.callback(interrupt)

    while True :
        pinC1.high ()
        
        start_time = utime.ticks_ms()
        running_time = utime.ticks_ms()
        
        while (start_time + 1000) > running_time:
            running_time = utime.ticks_ms()
            if queue.empty() == False:
                print(queue.get())
        pinC1.low()
        print("END HEREEEEEEEEEEEEEEEE")
        time.sleep(30)


def interrupt(self):
    global pinC0 
    global queue
    global adc
    global pinC1
    value = adc.read()
    if queue.full() == False:
        queue.put(value)
# =============================================================================

if __name__ == "__main__":
    
    main()
    


    
    
    
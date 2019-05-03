# -*- coding: utf-8 -*-
#
## @privatesection - Stuff in this file doesn't need to be Doxygen-ed
#
#  @author jr

import pyb
import micropython
import gc
import pyplot

import cotask
import task_share
import print_task

import controller
import encoder
import motor

# Allocate memory so that exceptions raised in interrupt service routines can
# generate useful diagnostic printouts
micropython.alloc_emergency_exception_buf (100)

tim = pyb.Timer(1, freq= 1000)
pinC0 = pyb.Pin (pyb.Pin.board.PC0, pyb.Pin.ANALOG)
queue = task_share.Queue(float, 1000)
adc = pyb.ADC(pinC0)
pinC1 = pyb.Pin (pyb.Pin.board.PC1, pyb.Pin.OUT_PP)

def main():
    tim.callback(interrupt)
    pinC1.high ()
    
    while queue.empty == False:
        print(queue.get())
    
    pinC1.low()


 #   pyplot.plot (queue.get(),time, 'g--')
  #  pyplot.xlabel ("Time (fortnights)")
   # pyplot.ylabel ("Height (furlongs)")
    #pyplot.title ("Time Vs Height") 


def interrupt():
    value = adc.read()
    if queue.full() == False:
        queue.put(value)
# =============================================================================

if __name__ == "__main__":
    
    main()
    


    
    
    
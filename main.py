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
import pyb
import utime

# Allocate memory so that exceptions raised in interrupt service routines can
# generate useful diagnostic printouts
micropython.alloc_emergency_exception_buf (100)


GOING = const (0)
STOPPED = const (1)
PRINT = const (2)
    
def task_calculation ():
    ''' Function which runs for Task 1, which toggles twice every second in a
    way which is only slightly silly.  '''
    control = controller.Controller(0.1, 0)
    motor1 = motor.MotorDriver()
    encoder1 = encoder.Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, pyb.Timer(4))

    state = STOPPED
    start_count = utime.ticks_ms()
    running_count = utime.ticks_ms()
    
    while True:
        pwm = control.calculate(encoder1.get_position())
        motor1.set_duty_cycle(pwm)
        running_count = utime.ticks_ms()
        if state == STOPPED :
            control.clear_list()
            if (running_count > (start_count + 10000)) :
                control.set_setpoint(5000)
                start_count = utime.ticks_ms()
                state = GOING
        elif state == GOING :
            if (running_count > (start_count + 300)) :
                control.set_setpoint(0)
                encoder1.zero()
                start_count = utime.ticks_ms()
                state = PRINT
        elif state == PRINT :
            control.print_results()
            control.clear_list()
            print("print end")
            state = STOPPED
            
        yield (state)



# =============================================================================

if __name__ == "__main__":

    print ('\033[2JTesting scheduler in cotask.py\n')

    # Create a share and some queues to test diagnostic printouts
    share0 = task_share.Share ('i', thread_protect = False, name = "Share_0")
    q0 = task_share.Queue ('B', 6, thread_protect = False, overwrite = False,
                           name = "Queue_0")
    q1 = task_share.Queue ('B', 8, thread_protect = False, overwrite = False,
                           name = "Queue_1")

    # Create the tasks. If trace is enabled for any task, memory will be
    # allocated for state transition tracing, and the application will run out
    # of memory after a while and quit. Therefore, use tracing only for 
    # debugging and set trace to False when it's not needed
    motor1_task = cotask.Task (task_calculation, name = 'motor1_task', priority = 1,
                            period = 25, profile = True, trace = False)
    motor2_task = cotask.Task (task_calculation, name = 'motor2_task', priority = 2,
                            period = 25, profile = True, trace = False)
    cotask.task_list.append (motor1_task)
    cotask.task_list.append (motor2_task)
    
    # A task which prints characters from a queue has automatically been
    # created in print_task.py; it is accessed by print_task.put_bytes()

    # Run the memory garbage collector to ensure memory is as defragmented as
    # possible before the real-time scheduler is started
    gc.collect ()

    # Run the scheduler with the chosen scheduling algorithm. Quit if any 
    # character is sent through the serial por
    vcp = pyb.USB_VCP ()
    while not vcp.any ():
        cotask.task_list.pri_sched ()

    # Empty the comm port buffer of the character(s) just pressed
    vcp.read ()

    # Print a table of task data and a table of shared information data
    print ('\n' + str (cotask.task_list) + '\n')
    print (task_share.show_all ())
    print (control_task.get_trace ())
    print ('\r\n')


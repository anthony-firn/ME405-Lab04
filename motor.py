## @file motor_mendez_fortner.py
#  Brief doc for motor_mendez_fortner.py
#
#  Detailed doc for motor_mendez_fortner.py 
#
#  @author Anthony Fortner, Claudia Mendez
#
#  @date April 2, 2019
#
#  @package motor_mendez_fortner
#  Brief doc for the motor_mendez_fortner module
#
#  Detailed doc for the motor_mendez_fortner module
#
#  @author Anthony Fortner, Claudia Mendez
#
#  @copyright License Info
#
#  @date April 2, 2019

import pyb

## 
#
#  This class implements a motor driver for the ME405 board.
#  @author Anthony Fortner, Claudia Mendez
#  @date April 2, 2019
class MotorDriver:
    
    ## pinA10 enable pin, set high to enable Motor Controller
    pinA10 = pyb.Pin (pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    pinA10.high ()
    
    ## pinB4 Motor Controller forward control pin
      
    pinB4 = pyb.Pin (pyb.Pin.board.PB4, pyb.Pin.OUT_PP)
    
    ## pinB5 Motor Controller reverse control pin
    pinB5 = pyb.Pin (pyb.Pin.board.PB5, pyb.Pin.OUT_PP)
    _tim3 = pyb.Timer (3, freq=20000)
    _ch1 = _tim3.channel (1, pyb.Timer.PWM, pin=pinB4)
    _ch2 = _tim3.channel (2, pyb.Timer.PWM, pin=pinB5)
	
    ## Constructor for motor driver
	#
	#  Creates a motor driver by initializing GPIO
	#  pins and turning the motor off for safety.
    def __init__ (self):

        print ('Creating a motor driver')

        self._ch1.pulse_width_percent (0)
        self._ch2.pulse_width_percent (0)
        
	## This method sets the duty cycle to be sent
	#  to the motor to the given level. Positive values
	#  cause torque in one direction, negative values
	#  in the opposite direction.
	#  @param level A signed integer holding the duty
	#  cycle of the voltage sent to the motor. Range -100 to 100. 
    def set_duty_cycle (self, level):
        #print ('Setting duty cycle to ' + str (level))
        
        if (level > 0) :
            self._ch2.pulse_width_percent (0)
            self._ch1.pulse_width_percent (level)
        else:
            self._ch1.pulse_width_percent (0)
            self._ch2.pulse_width_percent (-level)

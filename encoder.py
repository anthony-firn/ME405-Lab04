## @file encoder.py
#  Brief doc for encoder.py
#
#  Detailed doc for encoder.py 
#
#  @author Anthony Fortner, Claudia Mendez
#
#  @copyright License Info
#
#  @date April 9, 2019
#
import pyb

## 
#
#  An encoder driver object to measure rotational position of a motor
#
#  Measurment is based on shortest movement on an integer ring mod 2^16\n
#  This means that the encoder needs to be measured at a frequency equal to:\n
#  freq = (target Rev/min) * (encoder ticks/revolution) * 5.09*10^-7
#
#  @author Anthony Fortner, Claudia Mendez
#  @date April 9, 2019

class Encoder:

    ##  Constructor for encoder driver
    #    
    #   @param pin1 pyb.Pin.board.XXX pin object that is connected to encoder
    #   @param pin2 pyb.Pin.board.XXX pin object that is connected to encoder
    #   @param timer pyb.Timer object with channels that can interface with pin1, and pin2
    
    def __init__(self, pin1, pin2, timer):
        self._pinA = pyb.Pin (pin1, pyb.Pin.IN)

        self._pinB = pyb.Pin (pin2, pyb.Pin.IN)
    
        self._tim = timer
        
        self._tim.init(prescaler= 0, period= 0xFFFF)
    
        ch2 = self._tim.channel (2, pyb.Timer.ENC_A, pin = self._pinA)
        ch1 = self._tim.channel (1, pyb.Timer.ENC_B, pin = self._pinB)    
        
        self._current_ticks = 0
        self._past_ticks = 0
        self._total = 0
        self._tim.counter(0)

        
    ## Gets the encoder's position 
    #    
    #  Output is in units of encoder ticks\n
    #  A positive value indicates a forward rotation\n
    #  A negative value indicates a reverse rotation
        
    def get_position(self):

        self._past_ticks = self._current_ticks
        self._current_ticks = self._tim.counter()
        self._delta_ticks = self._current_ticks - self._past_ticks
        
        # encoder position is assumed to be the shortest rotation within integer ring
        if self._delta_ticks > 32768:
            self._delta_ticks -= 65536
            
        elif self._delta_ticks < -32768:
            self._delta_ticks += 65536
            
        self._total += self._delta_ticks
        return self._total
        
    ## Zeros out the encoder
    #    
    # encoder tick accumulator is set to zero
        
    def zero(self):

        self._current_ticks = 0
        self._past_ticks = 0
        self._total = 0
        self._tim.counter(0)
   ## @file mainpage.py
   #  Includes documentation for the entire project shown on the documentation landing page.
   #
   #  @author Anthony Fortner, Claudia Mendez
   #
   #  @mainpage
   #
   #  @section sec_intro Introduction
   #  Our driver is used to help in the creation of a two-wheeled robot that can balance on it's own. 
   #  The robot is open-loop unstable and stable in closed-loop. The robot is 
   #  also able to receive a remote input from a user to drive the robot.  
   #
   #  @section sec_Motor Motor Driver
   # 
   #  @subsection subsec_pur Purpose 
   #  The purpose of the motor driver is to control the direction and speed of a motor. 
   #
   #  @subsection subsec_use Usage
   #  To use the motor driver the following format is used:
   #
   #  motor.MotorDriver()
   #  
   #  Please see motor.MotorDriver for more parameter specifications for the motor driver. 
   #  
   #  @subsection subsec_test Testing 
   #  To test if the driver worked properly we inputted two different speeds in the set_duty_cycle function
   #  of the driver to ensure that it changed speeds. We also tested to make sure that the motor would
   #  rotate in two different directions by inputting negative and positive values in the set_duty_cycle function. 
   #    
   #    
   #  @subsection subsec_bug Bugs and Limitations 
   #  There were no bugs in our code. As for limitations ,the set_duty_cycle function
   #  of the motor can only be set in a range of -100 to 100. 
   #    
   #
   #  @section sec_Encoder Encoder Driver
   #
   #  @subsection subsec_pur Purpose 
   #  The purpose of the encoder driver is to measure the rotational position of a motor. 
   #
   #  @subsection subsec_use Usage
   #  To use the encoder driver the following format is used:
   #
   #  encoder.Encoder(pin1, pin2, timer)
   #  
   #  Please see encoder.Encoder for more parameter specifications for the encoder driver. 
   #  
   #  @subsection subsec_test Testing 
   #  To test if the driver worked properly we rotated the 
   #  motor by hand in one direction to see if the position of the motor increased
   #  or decreased, which it did. We then moved the motor in the other direction 
   #  to test if the motor's position moved in the opposite direction, which it did. 
   #    
   #  @subsection subsec_bug Bugs and Limitations 
   #  There were no bugs in our code. As for limitations our driver measurment is based on shortest movement on an integer ring mod 2^16\n
   #  This means that the encoder needs to be measured at a frequency equal to:
   #
   #  freq = (target Rev/min) * (encoder ticks/revolution) * 5.09*10^-7
   #
   #  @section sec_Controller Controller Driver
   #
   #  @subsection subsec_pur Purpose 
   #  The purpose of the controller driver is to implement a proportional control loop. 
   #
   #  @subsection subsec_use Usage
   #  To use the controller driver the following format is used:
   #
   #  controller.Controller(kp, setpoint)
   #  
   #  Please see controller.Controller for more parameter specifications for the controller driver. 
   #  
   #  @subsection subsec_test Testing 
   #  To test if the driver worked properly we created a main function that 
   #  communicated with a host computer. The host comuputer commuicated over a
   #  serial interface that sets a variety of gain values. From those gain values,
   #  we checked to make sure a step response graph was produced with reasonable values.    
   #    
   #  @subsection subsec_bug Bugs and Limitations 
   #  There were no bugs in our code. As for limitations our driver is that you must
   #  frequently call calculate to get the actuation signal. 
   #
   #  @section sec_link GitHub Link
   #  To get access to all the code listed above please see the following link:
   #
   #  https://github.com/anthony4tner/ME405-Lab01 


'''
Based on the Freenove Tank Robot Kit for Raspberry Pi
Adapted by James Mathews for Rpi5 compatibility
02-Feb-2024
'''

import time
### gpiozero library replaces pigpiod library ###
# This library is compatible with Rpi 5 architecture
# Read more here https://gpiozero.readthedocs.io/en/stable/index.html
from gpiozero import Servo 
import tkinter as tk

# Suppress the PWMSoftwareFallback warning
import warnings
from gpiozero import PWMSoftwareFallback
warnings.filterwarnings("ignore", category=PWMSoftwareFallback)


### No need to define a class if using gpiozero
# The default 'Servo' class already meets our needs for this script

### No need to define a class if using gpiozero
# The default 'AngularServo' class already meets our needs for this script
# However, it can be defined as a custom PWM device for more fine-grained control
class Servo:
    '''
    Class to create an angular servo as a generic PWMOutputDevice
    Using gpiozero for pi5 compatibility
    '''
    def __init__(self, channel):
        '''
        Constructor for servo class using gpiozero PWMOutputDevice
        Inputs:
            channel (int): GPIO servo channel number 0-3
        Returns:
            Null
        '''
        # Map the available pins to existing Freenove channel no. in a dictionary
        # When calling the function, we can then just pass 0, 1, or 2 to refer to specific pins
        # Scoping these mappings only to the constructor to conserve memory
        channel_mappings = {
            0:7,
            1:8,
            2:25
        }
        # Scope the channel variable provided as the pin to this instance
        self.pin = channel_mappings[channel]
        self.channel = channel
        # Initialise the PWMOutputDevice class from gpiozero
        print(self.pin)
        self.PwmServo = PWMOutputDevice(self.pin, active_high=True, initial_value=0, frequency=50, pin_factory=None)

    # No need to pass the channel, we scoped that in the constructor
    def angle_range(self, init_angle):
        '''
        Defines the angle range desired for the servo
        Inputs:
            channel (int): Channel number
        Returns:
            init_angle (int): Angle in degrees
        '''
        # Different calculations depending on servo channel
        if self.channel==0:
            if init_angle<90 :
                init_angle=90
            elif init_angle>150 :
                init_angle=150
            else:
                init_angle=init_angle
        elif self.channel==1:
            if init_angle<90 :
                init_angle=90
            elif init_angle>150 :
                init_angle=150
            else:
                init_angle=init_angle
        elif self.channel==2:
            if init_angle<0 :
                init_angle=0
            elif init_angle>180 :
                init_angle=180
            else:
                init_angle=init_angle
        return init_angle
        
    def setServoPwm(self,angle):
        '''
        Sets the PWM cycle for the device
        *Not yet fully tested with gpiozero*
        Inputs:
            channel (int)
        '''
        if self.channel==0:
            # Calculate angle
            angle=int(self.angle_range(angle))
            # Pulse the servo
            self.PwmServo.pulse(self.pin,n=1)
        elif self.channel==1:
            angle=int(self.angle_range(angle))
            self.PwmServo.pulse(self.pin,n=1)
        elif self.channel==2:
            angle=int(self.angle_range(angle))
            self.PwmServo.pulse(self.pin,n=1)

#### Initialise the servo instances
## For simplicity,
## We will use the generic Servo class from gpiozero

servo_arm = Servo(8, frame_width = 1/50)
servo_hand = Servo(25, frame_width = 1/200)


if __name__ == '__main__':

    # Function to open the servo
    def open_servo():
        servo_hand.max()
        print("Opening the servo")

    # Function to close the servo
    def close_servo():
        servo_hand.min()
        print("Closing the servo")

    # Create open and close buttons
    open_button = tk.Button(window, text="Open Servo", command=open_servo)
    close_button = tk.Button(window, text="Close Servo", command=close_servo)

    # Pack the buttons into the window
    open_button.pack()
    close_button.pack()

    # Run the tkinter main loop
    window.mainloop()
            

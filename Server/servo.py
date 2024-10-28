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
from gpiozero import PWMOutputDevice
warnings.filterwarnings("ignore", category=PWMSoftwareFallback)


### No need to define a class if using gpiozero
# The default 'Servo' class already meets our needs for this script

### No need to define a class if using gpiozero
# The default 'AngularServo' class already meets our needs for this script
# However, it can be defined as a custom PWM device for more fine-grained control

class Servo:
    '''
    Class to create and control multiple angular servos as generic PWMOutputDevices
    using gpiozero for Pi compatibility.
    '''

    def __init__(self):
        '''
        Initializes servos for all channels using gpiozero PWMOutputDevice.
        '''
        # Map the available pins to their respective Freenove channel numbers
        channel_mappings = {
            0: 7,
            1: 8,
            2: 25
        }

        # Initialize PWMOutputDevice for each channel and store in a dictionary
        self.servos = {}
        #for channel, pin in channel_mappings.items():
        #    self.servos[channel] = PWMOutputDevice(pin, active_high=True, initial_value=0, frequency=50)

    def angle_range(self, channel, init_angle):
        '''
        Defines the angle range for the servo based on channel-specific constraints.
        
        Parameters:
            channel (int): Channel number (0, 1, or 2)
            init_angle (int): Desired angle in degrees
        
        Returns:
            int: Constrained angle in degrees
        '''
        # Set angle limits based on channel
        if channel == 0 or channel == 1:
            if init_angle < 90:
                init_angle = 90
            elif init_angle > 150:
                init_angle = 150
        elif channel == 2:
            if init_angle < 0:
                init_angle = 0
            elif init_angle > 180:
                init_angle = 180
        return init_angle

    def setServoPwm(self, channel, angle):
        '''
        Sets the PWM cycle for the specified servo channel.
        
        Parameters:
            channel (int): Servo channel number (0, 1, or 2)
            angle (int): Desired angle in degrees
        '''
                # Map the available pins to their respective Freenove channel numbers
        channel_mappings = {
            '0': 7,
            '1': 8,
            '2': 25
        }
        # Get the constrained angle for the specified channel
        angle = self.angle_range(channel, angle)
        
        # Convert angle to pulse width (assuming pulse width range is 1ms to 2ms)
        # You may need to adjust this formula based on your servo's requirements
        pulse_width = (angle / 180.0) + 1.0  # Mapping 0-180 to 1.0ms - 2.0ms
        
        # Set the pulse width on the servo's PWM output
        self.servos[channel] = PWMOutputDevice(channel_mappings[channel], active_high=True, initial_value=0, frequency=50)
        self.servos[channel].value = pulse_width / 20  # Normalize for PWM output range (0.05-0.10)

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
            

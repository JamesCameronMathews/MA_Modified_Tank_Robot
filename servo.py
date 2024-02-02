'''
Based on the Freenove Tank Robot Kit for Raspberry Pi
Adapted by James Mathews for Rpi5 compatibility
02-Feb-2024
'''

import time
### gpiozero library replaces pigpiod library ###
# This library is compatible with Rpi 5 architecture
# Read more here https://gpiozero.readthedocs.io/en/stable/index.html
from gpiozero import AngularServo, PWMOutputDevice

# Suppress the PWMSoftwareFallback warning
import warnings
from gpiozero import PWMSoftwareFallback
warnings.filterwarnings("ignore", category=PWMSoftwareFallback)


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

#### Main program logic follows:
if __name__ == '__main__':
    print("Now servo 0 will be rotated to 150° and servos 1 will be rotated to 90°.") 
    print("If they were already at 150° and 90°, nothing would be observed.")
    print("Please keep the program running when installing the servos.")
    print("After that, you can press ctrl-C to end the program.")
    
    #### Log to a file
    file = open('calibration.txt', 'w')
    file.write('ok')

    #### Initialise the servo instance on pin #8
    ## For simplicity, we will not use the custom class defined above,
    ## We will use the generic AngularServo class from gpiozero
    pin = 8
    servo = AngularServo(8, min_angle=-90, max_angle=90)
    
    # Loop using default AngularServo class
    while True:
        servo.angle = 0
        file.write(f'Servo angle: {servo.angle}')
        time.sleep(2)
        servo.angle = 90
        file.write(f'Servo angle: {servo.angle}')
        time.sleep(2)
        servo.angle = 0
        file.write(f'Servo angle: {servo.angle}')
        time.sleep(2)
        servo.angle = 45
        file.write(f'Servo angle: {servo.angle}')
        time.sleep(2)
        servo.angle = 90
        file.write(f'Servo angle: {servo.angle}')
        time.sleep(2)
        # Close the file
        file.write(f'Servo test completed')
        file.close()
        print ("\nEnd of program")
        break

    # # # Alternative loop using custom PWM class (tested, a bit more jittery than default AngularServo
    ## Use our custom class with channel 1 (refers to pin 8)
    # custom_servo = Servo(1)
    # while True:
 
    #     custom_servo.setServoPwm(150)
    #     custom_servo.setServoPwm(90)     
    #     time.sleep(2)
    #     # Close the file
    #     file.write(f'Servo test completed')
    #     file.close()
    #     print ("\nEnd of program")
    #     break
            

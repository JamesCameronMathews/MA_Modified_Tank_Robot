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


#### Initialise the servo instances
## For simplicity,
## We will use the generic Servo class from gpiozero

servo_arm = Servo(8, frame_width = 1/50)
servo_hand = Servo(25, frame_width = 1/200)


if __name__ == '__main__':
    # print("Now servo 1 will be set to the minimim, then middle, then maxiumum.") 
    # while True:
        
        # servo_arm.max()
        # print(f'Max: {servo_arm.value}')
        # time.sleep(1)
        # servo_arm.mid()
        # print(f'Mid: {servo_arm.value}')
        # time.sleep(1)
        # servo_arm.min()
        # print(f'Min: {servo_arm.value}')
        # time.sleep(1)
        # servo_arm.mid()
        # print(f'trying value')
        # servo_arm.value = 1.0
        # print(f'Max: {servo_arm.value}')
        # time.sleep(1)
        # servo_arm.value = 0.0
        # print(f'Mid: {servo_arm.value}')
        # time.sleep(1)
        # servo_arm.value = -1.0
        # print(f'Min: {servo_arm.value}')
        # time.sleep(1)
        # servo_arm.value = 0.0
        
        # break
    print("Now servo 0 will be set to the minimim, then middle, then maxiumum.") 
    #while True:
        # servo_hand.value = 1.0
        #servo_hand.max()
        #time.sleep(1)
        #servo_hand.min()
        #servo_hand.value = 0.0
        #time.sleep(1)
        #servo_hand.mid()
        #servo_hand.value = -1.0
        #time.sleep(1)
        #servo_hand.value = 0.0
        #break

    # Create a tkinter window
    window = tk.Tk()
    window.title("Servo Control")

    # Function to open the servo
    def open_servo():
        # Replace with code to open the servo
        # Example:
        servo_hand.max()
        print("Opening the servo")

    # Function to close the servo
    def close_servo():
        # Replace with code to close the servo
        # Example:
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
            

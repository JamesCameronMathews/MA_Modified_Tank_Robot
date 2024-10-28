import time
from gpiozero import Motor as zmotor # Alias to prevent conflict

class Motor:
    def __init__(self):
        # Access GPIO pins and create motor object
        self.pwm1 = 24
        self.pwm2 = 23
        self.pwm3 = 5
        self.pwm4 = 6         
        self.motorL = zmotor(forward=self.pwm1, backward=self.pwm2, pwm=True)
        self.motorR = zmotor(forward=self.pwm3, backward=self.pwm4, pwm=True)

    def setMotorModel(self,duty1,duty2):
        # Assign duties to each motor
        if duty1 > 0:
            self.motorL.forward()
        elif duty1 < 0:
            self.motorL.reverse()
        else:
            self.motorL.stop()
        if duty2 > 0:
            self.motorR.forward()
        elif duty2 < 0:
            self.motorR.reverse()
        else:
            self.motorR.stop()

# Define the motor object
# PWM=Motor()

def loop():
    # Testing loop
    PWM.setMotorModel(2000,2000)        #Forward
    time.sleep(1)
    PWM.setMotorModel(-2000,-2000)      #Back
    time.sleep(1)
    PWM.setMotorModel(2000,-2000)       #Left 
    time.sleep(1)
    PWM.setMotorModel(-2000,2000)       #Right    
    time.sleep(1)
    PWM.setMotorModel(0,0)          #Stop
    time.sleep(1)
    
def destroy():
    PWM.setMotorModel(0,0)

if __name__=='__main__':
    print ('Program is starting ... \n')
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()

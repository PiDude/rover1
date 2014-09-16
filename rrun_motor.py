

import RPi.GPIO as GPIO
import sys
import time
import os


GPIO.setmode(GPIO.BCM)

# shutdown button
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)  

# right gearbox
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#left gearbox
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


#PWM_FREQ=50  #50Hz
#GPIO.PWM(23, PWM_FREQ)
#GPIO.PWM(17, PWM_FREQ)
#GPIO.PWM(20, PWM_FREQ)
#GPIO.PWM(21, PWM_FREQ)



def Shutdown(channel):
    os.system("sudo shutdown -h now")
	

GPIO.add_event_detect(4, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)   




# a = stop
# q = forward
# p = reverse
# w = right
# o = left
# n = exit


char = ''

while True:
    char = ''
    char = raw_input()

    if (char == 'n'):   # quit program
        break

    elif (char == 'a'):  # stop the wheels
        
        GPIO.output(23, False)
        GPIO.output(24, False)

        GPIO.output(20, False)
        GPIO.output(21, False)

    elif (char == 'q'):  # go forward
        
        GPIO.output(23, True)
        GPIO.output(24, False)
        
        GPIO.output(20, True)
        GPIO.output(21, False)
        
    elif (char == 'p'):  # go backward

        GPIO.output(23, False)
        GPIO.output(24, True)

        GPIO.output(20, False)
        GPIO.output(21, True)


    elif (char == 'w'):    # turn left
        
        GPIO.output(23, True)
        GPIO.output(24, False)

        GPIO.output(20, False)
        GPIO.output(21, True)

    elif (char == 'o'):    # turn right
        GPIO.output(23, False)
        GPIO.output(24, True)

        GPIO.output(20, True)
        GPIO.output(21, False)
        


print 'done'

GPIO.cleanup()




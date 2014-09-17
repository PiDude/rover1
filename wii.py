

import RPi.GPIO as GPIO
import sys
import time
import os
import cwiid


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

print 'press 1 + 2 on the Wii remote.....\n'

wii = None
i = 2

while not wii:
    try:
        wii = cwiid.Wiimote()
    except RuntimeError:
        if (i>10):
            quit()
            break

        print 'Error connecting to Wii remote. trying again...'
        i = i +1


print 'Wii remote connected !\n'

wii.rpt_mode = cwiid.RPT_BTN


while True:

    buttons = wii.state['buttons']

    # quit if press + and - buttons together'

    if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
        print '\nClosing connection....'
        wii.rumble = 1
        time.sleep(0.5)
        wii.rumble = 0
        GPIO.cleanup()
        exit(wii)

    elif (buttons & cwiid.BTN_UP):  # go forward
        
        GPIO.output(23, True)
        GPIO.output(24, False)
        
        GPIO.output(20, True)
        GPIO.output(21, False)
        
    elif (buttons & cwiid.BTN_DOWN):  # go backward

        GPIO.output(23, False)
        GPIO.output(24, True)

        GPIO.output(20, False)
        GPIO.output(21, True)


    elif (buttons & cwiid.BTN_LEFT):    # turn left
        
        GPIO.output(23, True)
        GPIO.output(24, False)

        GPIO.output(20, False)
        GPIO.output(21, True)

    elif (buttons & cwiid.BTN_RIGHT):    # turn right
        GPIO.output(23, False)
        GPIO.output(24, True)

        GPIO.output(20, True)
        GPIO.output(21, False)
        
    else:
        GPIO.output(23, False)
        GPIO.output(24, False)

        GPIO.output(20, False)
        GPIO.output(21, False)


print 'done'

GPIO.cleanup()




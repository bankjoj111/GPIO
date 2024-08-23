import RPi.GPIO as GPIO
import time 
led = 11
sw = 15
count = 0
state = 0    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led , GPIO.OUT)
GPIO.setup(sw , GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while True :
        if GPIO.wait_for_edge(sw , GPIO.FALLING):
            count = count + 1
            state = not(state)
            GPIO.output(led , state)
        if state :
            print(f"Button Pressed {count} : LED => ON ")
        else :
            print(f"Button Pressed {count} : LED => OFF ")

except KeyboardInterrupt:
    GPIO.cleanup()

print("\nbye...")
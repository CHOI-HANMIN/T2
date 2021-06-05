import RPi.GPIO as GPIO
import I2C_driver as LCD
from time import *

LCD = LCD.lcd()
SWC= 10
LED=11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWC, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
while True:
    LCD.lcd_clear()
    if GPIO.input(SWC) == GPIO.HIGH:
        LCD.lcd_display_string("LED ON",1)
        GPIO.output(LED, GPIO.HIGH)
    else:
        LCD.lcd_display_string("LED OFF",2)
        GPIO.output(LED, GPIO.LOW)

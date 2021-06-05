import RPi.GPIO as GPIO
import I2C_driver as LCD
from time import *

mylcd = LCD.lcd()
Switch= 10
LED=11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
while True:
    mylcd.lcd_clear()
    if GPIO.input(Switch) == GPIO.HIGH:
        mylcd.lcd_display_string("LED ON",1)
        GPIO.output(LED, GPIO.HIGH)
    else:
        mylcd.lcd_display_string("LED OFF",2)
        GPIO.output(LED, GPIO.LOW)

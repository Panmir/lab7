import drivers
import RPi.GPIO as GPIO
from time import sleep

SW1 = 24 
SW2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
display = drivers.Lcd()
display.lcd_clear()
try:
    while True:
        if GPIO.event_detected(SW1):
            print("SW1 pressed")
            display.lcd_display_string("P", 1)
            display.lcd_display_string("1165104620356", 2)
            sleep(2)
            display.lcd_display_string("Tan", 1)
            display.lcd_display_string("1165104620331", 2)
        elif GPIO.event_detected(SW2):
            print("SW2 pressed")
            display.lcd_clear()
            print("\nBye...")

except KeyboardInterrupt:
    display.lcd_clear()
    print("\nBye...")

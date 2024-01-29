import drivers
import RPi.GPIO as GPIO
from time import sleep

mt = ""
index = 0

SW1 = 24 
SW2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
display = drivers.Lcd()
display.lcd_clear()
display.lcd_display_string(mt+"LAB 7", 1)
try:
    while True:
        if GPIO.event_detected(SW1):
            if index+1 <= 11:
                index=index+1
                mt +=" "
                display.lcd_clear()
                display.lcd_display_string(mt+"LAB 7", 1)
                display.lcd_display_string(str(index),2)
            sleep(0.5)
        elif GPIO.event_detected(SW2):
            if index-1 >= 0:
                index=index-1
                mt = mt[1:]
                display.lcd_clear()
                display.lcd_display_string(mt+"LAB 7", 1)
                display.lcd_display_string(str(index),2)
            sleep(0.5)

except KeyboardInterrupt:
    GPIO.remove_event_detect(SW1)
    GPIO.remove_event_detect(SW2)
    display.lcd_clear()
    print("\nBye...")

import drivers
import RPi.GPIO as GPIO
from time import sleep
NAME = ["P","T"]
NUMBER = ["1165104620356","1165104620331"]

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
try:
    while True:
        if GPIO.event_detected(SW1):
            index = (index+1)%2
            display.lcd_clear()
            display.lcd_display_string(NAME[index], 1)
            display.lcd_display_string(NUMBER[index], 2)
            sleep(0.5)
        elif GPIO.event_detected(SW2):
            print("SW2 pressed")
            display.lcd_clear()
            print("\nBye...")
            exit()

except KeyboardInterrupt:
    GPIO.remove_event_detect(SW1)
    GPIO.remove_event_detect(SW2)
    display.lcd_clear()
    print("\nBye...")

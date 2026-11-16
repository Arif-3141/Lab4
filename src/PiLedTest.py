import time
from time import sleep
from hal import hal_led as led
import RPi.GPIO as GPIO #import RPi.GPIO module

FREQ_HZ = 10
DELAY = 1 / (2 * FREQ_HZ)
DELAY1 = 1 / (2 * 5)

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
    led.init()

def blink_led(delay):
    # Led Blink

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def off_led():
    led.set_output(0, 0)
    time.sleep(0.1)


def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1

    return ret


def main():
    init()
    while True:
        if read_slide_switch() == 1:
            blink_led(DELAY)
        elif read_slide_switch() == 0:
            blink_led(DELAY1)


if __name__ == "__main__":
    main()
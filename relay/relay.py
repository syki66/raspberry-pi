import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

print("setup")
time.sleep(2)

while(1):
    GPIO.output(18,True)
    print("true")
    time.sleep(0.02)

    GPIO.output(18,False)
    print("false")
    time.sleep(0.02)

GPIO.cleanup()
print("cleanup")
time.sleep(2)
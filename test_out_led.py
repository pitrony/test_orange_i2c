from time import sleep
import OPi.GPIO as GPIO
GPIO.setboard(GPIO.H616)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

counter=0
try:
   print ("Press CTRL+C to exit")
   while(counter<100):
     GPIO.output(12, 1)
     sleep(1)
     GPIO.output(12, 0)
     sleep(1)
     GPIO.output(7, 1)
     sleep(1)
     GPIO.output(7, 0)
     sleep(1)
     GPIO.output(11, 1)
     sleep(1)
     GPIO.output(11, 0)
     sleep(1)
     counter +=1
#GPIO.output(18, False)
except KeyboardInterrupt:
    GPIO.output(12, 0)
    GPIO.output(7, 0)
    GPIO.output(11, 0)
               # set port/pin value to 0/LOW/False
    GPIO.cleanup()              # Clean GPIO
    print ("Bye.")

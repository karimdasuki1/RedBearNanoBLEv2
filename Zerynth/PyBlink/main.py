# PyBlink
# Created at 2018-06-27 07:30:35.133025

led_1 = D11
pinMode(led_1, OUTPUT)
 
# Define the 'blink' function to be used by the threads
def blink(pin,timeON=100,timeOFF=100): # timeON and timeOFF are optional parameters, used as default
   while True:
       digitalWrite(pin,HIGH)   # turn the LED ON by making the voltage HIGH
       sleep(timeON)            # wait for timeON
       digitalWrite(pin,LOW)    # turn the LED OFF by making the voltage LOW
       sleep(timeOFF)           # wait for timeOFF
 
# Create threads that execute instances of the 'blink' function.
thread(blink,led_1) 
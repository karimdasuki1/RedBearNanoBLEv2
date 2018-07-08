# IfLED
# Created at 2018-06-27 06:28:14.166423

led_1 = D11
pinMode(led_1, OUTPUT)
import streams
streams.serial() 

while True:
       a=random(0,100)
       print(a)
       if a<50 :
            print("ON")
            digitalWrite(led_1,HIGH)   # turn the LED ON by making the voltage HIGH
            sleep(1000)            # wait for timeON
       else:
            print("OFF")
            digitalWrite(led_1,LOW)    # turn the LED OFF by making the voltage LOW
            sleep(1000)           # wait for timeOFF

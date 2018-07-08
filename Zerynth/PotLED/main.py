# PotLED
# Created at 2018-06-27 06:32:46.299130



import streams  # import the streams module
import adc
streams.serial() 
led_1 = D11
pinMode(led_1, OUTPUT)
while True:
    a = adc.read(A2)
    print(a)
    if a<512 :
        print("ON")
        digitalWrite(led_1,HIGH)   # turn the LED ON by making the voltage HIGH
        sleep(1000)            # wait for timeON
    else:
        print("OFF")
        digitalWrite(led_1,LOW)    # turn the LED OFF by making the voltage LOW
        sleep(1000)           # wait for timeOFF
    
    print("One sample:",a)
    print()
    sleep(300)
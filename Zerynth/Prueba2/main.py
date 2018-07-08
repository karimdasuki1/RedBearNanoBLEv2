# Prueba2
# Created at 2018-06-27 18:26:27.810830

import streams  # import the streams module
import adc
from nordic.nrf52_ble import nrf52_ble as bledrv
from wireless import ble

streams.serial()
bledrv.init()
ble.gap("RBNBLE1")
s = ble.Service(0x1818)
c = ble.Characteristic(0x2A65,ble.NOTIFY | ble.READ | ble.WRITE,1,"cY",ble.NUMBER)
s.add_characteristic(c)
ble.add_service(s)
ble.start()
ble.start_advertising()

led_1 = D11
pinMode(led_1, OUTPUT)


while True:
    a = adc.read(A2)
    c.set_value(a)
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
    



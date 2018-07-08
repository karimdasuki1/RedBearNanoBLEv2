# Servicio1
# Created at 2018-06-19 22:26:09.099320
# Prueba de un Services con dos Characteristics

import streams
# import a BLE driver: in this example we use NRF52
from nordic.nrf52_ble import nrf52_ble as bledrv
# then import the BLE modue
from wireless import ble

streams.serial()

# initialize NRF52 driver
bledrv.init()

# Set GAP name
ble.gap("RBKarim1")

# Create a GATT Service: let's try a Battery Service (uuid is 0x180F)
#s = ble.Service(0x180F)
ss = ble.Service(0x181C)

# Create a GATT Characteristic: (uuid for Battery Level is 0x2A19, and it is an 8-bit number)
#c1 = ble.Characteristic(0x2A19,ble.NOTIFY | ble.READ,1,"Battery Level",ble.NUMBER)
c2 = ble.Characteristic(0x2A59,ble.READ,1,"Analog Output",ble.NUMBER)
# Add the GATT Characteristic to the Service
#s.add_characteristic(c1)
ss.add_characteristic(c2)
# Add the Service
#ble.add_service(s)
ble.add_service(ss)
# Start the BLE stack
ble.start()

# Begin advertising
ble.start_advertising()


while True:
    print(".")
    sleep(1000)
    # Let's update the Characteristic Value
    #c1.set_value(random(0,100))
    c2.set_value(random(0,100))
    print(c2)
    
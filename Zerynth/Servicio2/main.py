# Servicio2
# Created at 2018-06-26 20:49:43.935602

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

# Create a GATT Service: let's try a Enviromental Sensing (uuid is 0x181A)
s = ble.Service(0x181A)

# Create a GATT Characteristic: (uuid for Battery Level is 0x2A19, and it is an 8-bit number)
c = ble.Characteristic(0x2A6A,ble.NOTIFY | ble.READ,1,"Temperature",ble.NUMBER)

# Add the GATT Characteristic to the Service
s.add_characteristic(c)

# Add the Service
ble.add_service(s)

# Start the BLE stack
ble.start()

# Begin advertising
ble.start_advertising()


while True:
    print(".")
    sleep(1000)
    # Let's update the Characteristic Value
    c.set_value(random.uniform(1.5, 1.9))
    
    
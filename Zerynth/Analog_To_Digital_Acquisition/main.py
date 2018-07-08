################################################################################
# Analog Read
# 
# Created by Zerynth Team 2015 CC
# Authors: G. Baldi, D. Mazzei
################################################################################

import streams  # import the streams module
import adc      # import the adc driver 
# create a stream linked to the default serial port
streams.serial() 

while True:
    
# Basic usage of ADC for acquiring the analog signal from a pin   
    value = adc.read(A0)
    print("One sample:",value)
    
    print()
    sleep(300)
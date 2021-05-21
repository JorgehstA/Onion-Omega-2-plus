import time
import onionGpio

"""
Establecer GPIO como salida y alternar entre LOW y HIGH
"""
gpioNum = 1
gpioObj = onionGpio.OnionGpio(gpioNum)

## set to output
status  = gpioObj.setOutputDirection(0)

## alternate the value
loop    = 1
value   = 0
while loop == 1:
    # reverse the value
    if value == 0:
        value = 1
    else:
        value = 0

    # set the new value
    status  = gpioObj.setValue(value)
    print 'GPIO%d set to: %d'%(gpioNum, value)

    time.sleep(5)
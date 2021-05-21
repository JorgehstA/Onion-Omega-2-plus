import time
import onionGpio

"""
Establecer GPIO como salida  y lectura del valor
"""

gpioNum = 6
gpioObj = onionGpio.OnionGpio(gpioNum)

## set to input
status  = gpioObj.setOutputDirection()
print 'GPIO%d set to output,'%(gpioNum),

## read the value
value   = gpioObj.getValue()
print ' initial value: %d'%(int(value))
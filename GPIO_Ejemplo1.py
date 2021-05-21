import time
import onionGpio

"""
Establecer GPIO como entrada y leer y mostrar el valor cada segundo
"""

gpioNum = 7
gpioObj = onionGpio.OnionGpio(gpioNum)

## set to input
status  = gpioObj.setInputDirection()

## read and print the value once a second
loop = 1
while loop == 1:
    value = gpioObj.getValue()
    print 'GPIO%d input value: %d'%(gpioNum, int(value))

    time.sleep(1)



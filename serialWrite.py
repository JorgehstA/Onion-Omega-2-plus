import serial
ser = serial.Serial('/dev/ttyS1') # open serial port
print(ser.name) # check which port was really used
ser.write(b'hello') # write a string
ser.write('copy?')
ser.close() # close port

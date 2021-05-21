import serial
with serial.Serial('/dev/ttyS1', 9600, timeout=10) as ser:
	line = ser.readline()
	print(line)

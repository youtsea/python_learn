import serial

ser = serial.Serial('COM1', baudrate=9600, bytesize=8, parity='N', stopbits=1)
ser.write(b'G1 X5 Y50 \r\n')
resp = serial.readline()
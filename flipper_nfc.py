import serial, time

f = serial.Serial('COM3', 115200, timeout=3)
time.sleep(1)
f.write(b'\r\n')
time.sleep(0.5)
f.read(2048)

f.write(b'nfc\r\n')
time.sleep(1)
f.read(2048)

f.write(b'apdu -p 4a -d 9060000000\r\n')
time.sleep(0.8)
print('Frame 1:', f.read(2048).decode('utf-8', errors='ignore'))

f.write(b'apdu -p 4a -d 90AF000000\r\n')
time.sleep(0.8)
print('Frame 2:', f.read(2048).decode('utf-8', errors='ignore'))

f.write(b'apdu -p 4a -d 90AF000000\r\n')
time.sleep(0.8)
print('Frame 3:', f.read(2048).decode('utf-8', errors='ignore'))

f.close()

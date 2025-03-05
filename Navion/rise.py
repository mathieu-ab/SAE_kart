import serial
import time

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Allow JeVois to initialize

# Send command to enable serial output
ser.write(b"setpar serout All\n")
time.sleep(1)  # Short delay after sending the command

# Read and print detection data
while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            print(line)
    except KeyboardInterrupt:
        break

ser.close()

import serial

ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

for param in ["serout", "width", "height"]:
    ser.write(f"getpar {param}\n".encode())
    print(f"{param}:", ser.readline().decode('utf-8', errors='ignore').strip())

ser.close()

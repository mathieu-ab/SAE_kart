import serial
import time

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Allow JeVois to initialize

# Send command to enable serial output
ser.write(b"setpar serout All\n")
time.sleep(1)  # Short delay after sending the command

print("Reading JeVois output in hexadecimal format...")

try:
    while True:
        # Read a line from the camera
        data = ser.readline()

        if data:
            # Convert to hexadecimal format
            hex_output = " ".join(f"{byte:02X}" for byte in data)
            print(hex_output)

except KeyboardInterrupt:
    print("\nStopping...")
    ser.close()

import serial
import time

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Allow JeVois to initialize

# Send command to enable serial output
ser.write(b"setpar serout All\n")
time.sleep(1)  # Short delay after sending the command

def classify_position(x_center):
    """Classify object position based on x_center value."""
    if x_center < -750:
        return "Left"
    elif -750 <= x_center <= 325:
        return "Center"
    else:
        return "Right"

while True:
    try:
        # Read a line from JeVois
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        
        if line.startswith("N2 person"):  # Ensure we process only person detections
            parts = line.split()
            x_center = int(parts[2])  # Extract x_center value
            
            position = classify_position(x_center)
            print(f"Person detected at {position} (x_center={x_center})")

    except KeyboardInterrupt:
        print("\nStopping...")
        break

ser.close()

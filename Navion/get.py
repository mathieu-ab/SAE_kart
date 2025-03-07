import serial
import time

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Allow JeVois to initialize

# Send command to enable serial output
ser.write(b"setpar serout All\n")
time.sleep(1)  # Short delay after sending the command

# Reference values for known distances
REF_HEIGHT_1M40 = 1350  # Approximate height at 1.4m
REF_HEIGHT_2M40 = 1075  # Approximate height at 2.4m
REF_HEIGHT_3M40 = 1147  # Approximate height at 3.4m

REF_DISTANCE_1M40 = 1.4  # meters
REF_DISTANCE_2M40 = 2.4  # meters
REF_DISTANCE_3M40 = 3.4  # meters

# Distance thresholds
DISTANCE_THRESHOLDS = {
    "far": 3.0,   
    "medium": 1.5,  
    "near": 0.0  
}

def estimate_distance(current_height):
    """Estimate distance using proportional scaling (cross-multiplication)."""
    if current_height <= 0:
        return "Unknown"

    if current_height >= REF_HEIGHT_1M40:
        return REF_DISTANCE_1M40 * REF_HEIGHT_1M40 / current_height
    elif current_height >= REF_HEIGHT_2M40:
        return REF_DISTANCE_2M40 * REF_HEIGHT_2M40 / current_height
    else:
        return REF_DISTANCE_3M40 * REF_HEIGHT_3M40 / current_height

while True:
    try:
        # Read a line from JeVois
        line = ser.readline().decode('utf-8', errors='ignore').strip()

        if line.startswith("N2 person"):  
            parts = line.split()
            height = int(parts[5])  # Extract bounding box height

            # Estimate distance
            estimated_distance = estimate_distance(height)
            print(f"Estimated Distance: {estimated_distance:.2f} meters")

    except Exception as e:
        print(f"Error: {e}")
        break

print("Connection closed.")
ser.close()

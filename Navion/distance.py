import serial

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Reference values for known distances
REF_HEIGHT_1M40 = 1350  # Approximate height at 1.4m
REF_HEIGHT_2M40 = 1075  # Approximate height at 2.4m
REF_HEIGHT_3M40 = 1147  # Approximate height at 3.4m

REF_DISTANCE_1M40 = 1.4  # meters
REF_DISTANCE_2M40 = 2.4  # meters
REF_DISTANCE_3M40 = 3.4  # meters

def estimate_distance(current_height):
    """Estimate distance using proportional scaling (cross-multiplication)."""
    if current_height <= 0:
        return "Unknown"

    # Use the reference height closest to the detected value
    if current_height >= REF_HEIGHT_1M40:  # Closer than 1.4m
        return REF_DISTANCE_1M40 * REF_HEIGHT_1M40 / current_height
    elif current_height >= REF_HEIGHT_2M40:  # Between 1.4m and 2.4m
        return REF_DISTANCE_2M40 * REF_HEIGHT_2M40 / current_height
    else:  # Greater than 2.4m (farther away)
        return REF_DISTANCE_3M40 * REF_HEIGHT_3M40 / current_height

while True:
    try:
        # Read a line from JeVois
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        
        if line.startswith("N2 person"):  # Process only person detections
            parts = line.split()
            x_center = int(parts[2])  # Extract x_center for position
            height = int(parts[5])  # Extract bounding box height

            # Determine position
            if x_center < -750:
                position = "Left"
            elif -750 <= x_center <= 325:
                position = "Center"
            else:
                position = "Right"

            # Estimate distance
            estimated_distance = estimate_distance(height)
            
            print(f"Person detected at {position}, Distance: {estimated_distance:.2f}m (h={height})")

    except KeyboardInterrupt:
        print("\nStopping...")
        break

ser.close()

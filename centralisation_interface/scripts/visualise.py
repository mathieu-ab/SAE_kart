import serial

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)

# Reference values for known distances
REF_HEIGHT_1M40 = 1350  # Approximate height at 1.4m
REF_HEIGHT_2M40 = 1075  # Approximate height at 2.4m
REF_HEIGHT_3M40 = 1147  # Approximate height at 3.4m

REF_DISTANCE_1M40 = 1.4  # meters
REF_DISTANCE_2M40 = 2.4  # meters
REF_DISTANCE_3M40 = 3.4  # meters

# Distance thresholds
DISTANCE_THRESHOLDS = {
    "far": 3.0,     # 3m and above → Far
    "medium": 1.5,  # 1.5m to 3m → Medium
    "near": 0.0     # Below 1.5m → Near
}

def estimate_distance(current_height):
    """Estimate distance using proportional scaling."""
    if current_height <= 0:
        return None  # Invalid distance

    if current_height >= REF_HEIGHT_1M40:  # Closer than 1.4m
        return REF_DISTANCE_1M40 * REF_HEIGHT_1M40 / current_height
    elif current_height >= REF_HEIGHT_2M40:  # Between 1.4m and 2.4m
        return REF_DISTANCE_2M40 * REF_HEIGHT_2M40 / current_height
    else:  # Greater than 2.4m (farther away)
        return REF_DISTANCE_3M40 * REF_HEIGHT_3M40 / current_height

def classify_distance(distance):
    """
    Classifies the distance into Far, Medium, or Near.
    """
    if distance is None:
        return "Unknown"

    if distance >= DISTANCE_THRESHOLDS["far"]:
        return "Far"
    elif DISTANCE_THRESHOLDS["medium"] <= distance < DISTANCE_THRESHOLDS["far"]:
        return "Medium"
    else:
        return "Near"
def run(interface) :
    while True:
        try:
            # Read a line from JeVois
            line = ser.readline().decode('utf-8', errors='ignore').strip()

            if line.startswith("N2 person"):  # Process only person detections
                parts = line.split()
                height = int(parts[5])  # Extract bounding box height

                # Estimate distance
                estimated_distance = estimate_distance(height)
                distance_category = classify_distance(estimated_distance)

                # Print result directly on Raspberry Pi
                print(f"{distance_category}: {estimated_distance:.2f}m")

        except Exception as e:
            print(f"Error: {e}")
            break

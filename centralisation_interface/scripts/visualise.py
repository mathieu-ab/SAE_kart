import serial
from module_import import *  # Now try importing


# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)

# Reference values for known distances
REF_HEIGHT_1M40 = 1350  
REF_HEIGHT_2M40 = 1075  
REF_HEIGHT_3M40 = 1147  

REF_DISTANCE_1M40 = 1.4  
REF_DISTANCE_2M40 = 2.4  
REF_DISTANCE_3M40 = 3.4  

# Distance thresholds
DISTANCE_THRESHOLDS = {
    "far": 3.0,   
    "medium": 1.5,  
    "near": 0.0  
}

def estimate_distance(current_height):
    """Estimate distance using proportional scaling."""
    if current_height <= 0:
        return None  

    if current_height >= REF_HEIGHT_1M40:  
        return REF_DISTANCE_1M40 * REF_HEIGHT_1M40 / current_height
    elif current_height >= REF_HEIGHT_2M40:  
        return REF_DISTANCE_2M40 * REF_HEIGHT_2M40 / current_height
    else:  
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

def update_ui(distance_category, interface):
    """
    Updates a single UI element based on the distance classification.
    """
    if distance_category == "Far":
        # Example: Show "Obstacle Gauche Arc 1" when far
        interface.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc 1").show = True
    else:
        # Hide otherwise
        interface.container_storage["aide"]["Nav Radar"].get_object("Obstacle Gauche Arc 1").show = False

def run(interface) :
    while True:
        try:
            # Read a line from JeVois
            line = ser.readline().decode('utf-8', errors='ignore').strip()

            if line.startswith("N2 person"):  
                parts = line.split()
                height = int(parts[5])  

                # Estimate distance
                estimated_distance = estimate_distance(height)
                distance_category = classify_distance(estimated_distance)

                # Print result
                print(f"{distance_category}: {estimated_distance:.2f}m")

                # Update UI element visibility based on classification
                update_ui(distance_category, interface)

        except Exception as e:
            print(f"Error: {e}")
            break

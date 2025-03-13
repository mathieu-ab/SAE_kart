import serial
import time
import paho.mqtt.client as mqtt

# MQTT Broker Configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC_DISTANCE = "kart/distance"
MQTT_TOPIC_SPEED = "autonomie/vitesse"

# Initialize MQTT client
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
time.sleep(2)  # Allow JeVois to initialize

# Send command to enable serial output
ser.write(b"setpar serout All\n")
time.sleep(1)  # Short delay after sending the command

# Tracking system for multiple objects
tracked_objects = {}  # Stores {ID: (x_center, y_center, frame_count)}
available_ids = []  # List of reusable IDs
next_id = 1  # Unique ID counter
FRAME_THRESHOLD = 5  # Number of frames before an object is removed
X_THRESHOLD = 50  # Maximum movement in x_center to consider the same object

# Reference values for known distances
REF_HEIGHT_1M40 = 1350  # Approximate height at 1.4m
REF_HEIGHT_2M40 = 1075  # Approximate height at 2.4m
REF_HEIGHT_3M40 = 1147  # Approximate height at 3.4m

REF_DISTANCE_1M40 = 1.4  # meters
REF_DISTANCE_2M40 = 2.4  # meters
REF_DISTANCE_3M40 = 3.4  # meters

# Distance thresholds
DISTANCE_THRESHOLDS = {
    "far": 7.50,   
    "medium": 3.65,  
    "near": 0.0  
}

# Speed constraints
V_MAX = 20  # Maximum speed value
D_MAX = 10   # Maximum detection range
D_STOP = 2   # Stop distance threshold

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

def classify_distance(distance):
    if distance is None:
        return "Unknown"

    if distance >= DISTANCE_THRESHOLDS["far"]:
        return "Far"
    elif DISTANCE_THRESHOLDS["medium"] <= distance < DISTANCE_THRESHOLDS["far"]:
        return "Medium"
    else:
        return "Near"

def calculate_speed(distance):
    """Calculate speed based on distance using a linear equation."""
    if distance is None or distance <= D_STOP:
        return 0  # Stop at 2m
    elif distance >= D_MAX:
        return V_MAX  # Full speed at 10m
    else:
        return V_MAX * (distance - D_STOP) / (D_MAX - D_STOP)  # Linear scaling

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if not line:
            continue

        print(f"Raw Detection: {line}")

        if line.startswith("N2 person"):  # Process only person detections
            parts = line.split()
            try:
                confidence = int(parts[1].split(":")[1])  # Extract confidence after 'person:'
                x_center = int(parts[2])  # Extract x_center
                height = int(parts[5])  # Extract bounding box height
            except (IndexError, ValueError) as e:
                print(f"Parsing error: {e}, skipping line: {line}")
                continue

            # Determine position
            if x_center < -750:
                position = "Left"
            elif -750 <= x_center <= 325:
                position = "Center"
            else:
                position = "Right"

            # Estimate distance
            estimated_distance = estimate_distance(height)
            distance_category = classify_distance(estimated_distance)
            speed = calculate_speed(estimated_distance)

            # Assign/reuse an ID for tracking
            matched_id = None
            for obj_id, (prev_x, _, frames) in tracked_objects.items():
                if abs(prev_x - x_center) <= X_THRESHOLD:
                    matched_id = obj_id
                    break

            if matched_id:
                tracked_objects[matched_id] = (x_center, height, FRAME_THRESHOLD)  # Reset frame count
            else:
                if available_ids:
                    matched_id = available_ids.pop(0)
                else:
                    matched_id = next_id
                    next_id += 1
                tracked_objects[matched_id] = (x_center, height, FRAME_THRESHOLD)

            # Construct the MQTT messages
            distance_message = f"{distance_category} {position}"
            speed_message = f"{speed:.2f}"
            
            # Publish to MQTT topics
            mqtt_client.publish(MQTT_TOPIC_DISTANCE, distance_message)
            mqtt_client.publish(MQTT_TOPIC_SPEED, speed_message)

            print(f"Object ID {matched_id} -> Distance: {estimated_distance:.2f}m, Position: {position}")
            print(f"Published Distance: {distance_message}")
            print(f"Published Speed: {speed_message}")

        # Reduce frame count and remove old objects
        to_remove = []
        for obj_id in list(tracked_objects.keys()):
            x, y, frames = tracked_objects[obj_id]
            if frames > 0:
                tracked_objects[obj_id] = (x, y, frames - 1)
            else:
                to_remove.append(obj_id)

        for obj_id in to_remove:
            del tracked_objects[obj_id]
            available_ids.append(obj_id)  # Reuse this ID in the future
            print(f"Object ID {obj_id} removed and now available for reuse.")

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")
        break

ser.close()

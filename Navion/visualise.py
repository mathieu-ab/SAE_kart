import serial
import socket
import paho.mqtt.client as mqtt
import time

# MQTT Broker Configuration
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC_DISTANCE = "kart/distance"
MQTT_TOPIC_SPEED = "autonomie/vitesse"

# Initialize MQTT client
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

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
        # Read a line from JeVois
        line = ser.readline().decode('utf-8', errors='ignore').strip()

        if line.startswith("N2 person"):  
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
            distance_category = classify_distance(estimated_distance)
            speed = calculate_speed(estimated_distance)

            # Construct the MQTT messages
            distance_message = f"{distance_category} {position}"
            speed_message = f"{speed:.2f}"
            
            # Publish to MQTT topics
            mqtt_client.publish(MQTT_TOPIC_DISTANCE, distance_message)
            mqtt_client.publish(MQTT_TOPIC_SPEED, speed_message)

            # Print results
            print(f"Published Distance: {distance_message}")
            print(f"Published Speed: {speed_message}")

    except Exception as e:
        print(f"Error: {e}")
        break

print("Connection closed.")
ser.close()
    
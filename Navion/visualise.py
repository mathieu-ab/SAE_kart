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

# Reference values for known distances
REF_HEIGHT_1M40 = 1350  
REF_HEIGHT_2M40 = 1075  
REF_HEIGHT_3M40 = 1147  

REF_DISTANCE_1M40 = 1.4  
REF_DISTANCE_2M40 = 2.4  
REF_DISTANCE_3M40 = 3.4  

# Distance thresholds
DISTANCE_THRESHOLDS = {
    "far": 7.50,   
    "medium": 3.65,  
    "near": 0.0  
}

# Speed constraints
V_MAX = 20  
D_MAX = 10   
D_STOP = 2   

# Time window for grouping detections (in seconds)
TIME_WINDOW = 0.1  # 100ms
last_publish_time = time.time()
frame_detections = []  # Buffer for detections in the same time window

def estimate_distance(current_height):
    """Estimate distance using proportional scaling."""
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
        return 0  
    elif distance >= D_MAX:
        return V_MAX  
    else:
        return V_MAX * (distance - D_STOP) / (D_MAX - D_STOP)  

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if not line:
            continue

        if line.startswith("N2 person"):  
            parts = line.split()
            try:
                confidence = int(parts[1].split(":")[1])  # Extract confidence percentage
                if confidence < 30:  # Ignore detections with confidence < 30%
                    continue

                x_center = int(parts[2])  
                height = int(parts[5])  
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

            # Estimate distance and speed
            estimated_distance = estimate_distance(height)
            distance_category = classify_distance(estimated_distance)
            speed = calculate_speed(estimated_distance)

            # Store detection in the current frame buffer
            frame_detections.append(f"{distance_category} {position}")

            # Check if it's time to publish detections
            if time.time() - last_publish_time >= TIME_WINDOW:
                if frame_detections:
                    message = " | ".join(frame_detections)  
                    mqtt_client.publish(MQTT_TOPIC_DISTANCE, message)
                    mqtt_client.publish(MQTT_TOPIC_SPEED, f"{speed:.2f}")

                    print(f"Published Distance: {message}")
                    print(f"Published Speed: {speed:.2f}")

                    # Clear detections for the next frame
                    frame_detections.clear()
                    last_publish_time = time.time()

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")
        break

ser.close()

import serial
import paho.mqtt.client as mqtt  # Import MQTT library

MQTT_BROKER = "localhost"  # Replace with your broker IP or hostname
MQTT_PORT = 1883  # Default MQTT port
MQTT_TOPIC = "kart/distance"  # Topic for publishing data

# Initialize MQTT client
mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)  # Connect to the MQTT broker

# Open serial connection to JeVois
ser = serial.Serial(
    port='/dev/ttyUSB1',   
    baudrate=115200,       
    parity=serial.PARITY_NONE,  
    stopbits=serial.STOPBITS_ONE,  
    bytesize=serial.EIGHTBITS,  
    timeout=1  
)

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

            # Construct the MQTT message
            message = distance_category
            
            # Publish to MQTT topic
            mqtt_client.publish(MQTT_TOPIC, message)

            # Print result
            print(f"Published: {message}")

    except Exception as e:
        print(f"Error: {e}")
        break

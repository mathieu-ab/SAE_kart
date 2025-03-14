import serial
import socket

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)

# Reference values for known distances
REF_HEIGHT_1M40 = 1350  # Approximate height at 1.4m
REF_HEIGHT_2M40 = 1075  # Approximate height at 2.4m
REF_HEIGHT_3M40 = 1147  # Approximate height at 3.4m

REF_DISTANCE_1M40 = 1.4  # meters
REF_DISTANCE_2M40 = 2.4  # meters
REF_DISTANCE_3M40 = 3.4  # meters

# TCP Server settings
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 65432      # Port for communication

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

# Start TCP server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server started. Waiting for connection on {HOST}:{PORT}...")

    conn, addr = server.accept()
    with conn:
        print(f"Connected by {addr}")
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
                    distance_data = f"{position},{estimated_distance:.2f}m\n"
                    
                    # Send data to connected PC
                    conn.sendall(distance_data.encode())

            except Exception as e:
                print(f"Error: {e}")
                break

print("Connection closed.")
ser.close()

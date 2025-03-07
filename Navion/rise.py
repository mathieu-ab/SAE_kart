import serial
import time

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Allow JeVois to initialize

# Send command to enable serial output
ser.write(b"setpar serout All\n")
time.sleep(1)  # Short delay after sending the command

# Tracking system for multiple objects
tracked_objects = {}  # Stores {ID: (x_center, y_center, frame_count)}
next_id = 1  # Unique ID counter
FRAME_THRESHOLD = 5  # Number of frames before an object is removed
X_THRESHOLD = 50  # Maximum movement in x_center to consider the same object

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
                y_center = int(parts[3])  # Extract y_center
                width = int(parts[4])  # Extract width
                height = int(parts[5])  # Extract height
            except (IndexError, ValueError) as e:
                print(f"Parsing error: {e}, skipping line: {line}")
                continue

            matched_id = None
            for obj_id, (prev_x, prev_y, frames) in tracked_objects.items():
                if abs(prev_x - x_center) <= X_THRESHOLD:
                    matched_id = obj_id
                    break

            if matched_id:
                tracked_objects[matched_id] = (x_center, y_center, FRAME_THRESHOLD)  # Reset frame count
            else:
                tracked_objects[next_id] = (x_center, y_center, FRAME_THRESHOLD)
                matched_id = next_id
                next_id += 1

            print(f"Object ID {matched_id} -> X: {x_center}, Y: {y_center}, Confidence: {confidence}")

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
            print(f"Object ID {obj_id} removed from tracking.")

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")
        break

ser.close()
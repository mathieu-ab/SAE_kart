import serial
import time
import numpy as np
from sklearn.linear_model import LinearRegression

# Reference data: Distance (m) based on Width (w) and Height (h)
distance_reference = np.array([0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
width_reference = np.array([1987, 2069, 1975, 2091, 1518, 1371, 1174, 942, 532, 575, 498, 389, 409, 400, 272, 265, 266, 256, 257, 265])
height_reference = np.array([1668, 1546, 1507, 1474, 1391, 1329, 1180, 1127, 952, 951, 950, 897, 777, 740, 511, 496, 447, 421, 418, 417])

# Preparing the regression model
X_train = np.column_stack((width_reference, height_reference))  # Combine width and height as input features
y_train = distance_reference  # Target: distance

model = LinearRegression()
model.fit(X_train, y_train)  # Train the model

# Function to estimate distance from width & height
def estimate_distance(w, h):
    return model.predict(np.array([[w, h]]))[0]

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)
time.sleep(2)  # Allow JeVois to initialize

# Enable serial output from JeVois
ser.write(b"setpar serout All\n")
time.sleep(1)

print("Reading data... Press Ctrl+C to stop.")

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        if line:
            parts = line.split()
            if len(parts) >= 5:  # Ensure we have enough data
                try:
                    w = int(parts[3])  # Extract width
                    h = int(parts[4])  # Extract height
                    estimated_distance = estimate_distance(w, h)
                    print(f"Width: {w} px, Height: {h} px → Estimated Distance: {estimated_distance:.2f} m")
                except ValueError:
                    print("Error parsing received data.")
    except KeyboardInterrupt:
        print("\nStopping program.")
        break

ser.close()

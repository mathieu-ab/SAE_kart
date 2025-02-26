import serial
import numpy as np

# Open serial connection to JeVois
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Reference data (Real vs Measured distances) for polynomial fitting
real_distances = np.array([140, 240, 340, 260, 150, 90])  # cm (True distances)
measured_distances = np.array([240, 270, 380, 275, 240, 130])  # Measured distances

# Fit a second-degree polynomial for correction
coeffs = np.polyfit(measured_distances, real_distances, 2)
poly_correction = np.poly1d(coeffs)

def estimate_corrected_distance(current_height):
    """Estimate distance using polynomial correction (Result in cm)."""
    return poly_correction(current_height)

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

            # Apply polynomial correction for distance estimation (keeps value in cm)
            estimated_distance = estimate_corrected_distance(height)
            
            print(f"Person detected at {position}, Distance: {estimated_distance:.2f} cm (h={height})")

    except KeyboardInterrupt:
        print("\nStopping...")
        break

ser.close()

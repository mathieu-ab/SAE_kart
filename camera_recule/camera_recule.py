import cv2
import numpy as np
import os

# Définir la variable d'environnement XDG_RUNTIME_DIR
os.environ["XDG_RUNTIME_DIR"] = f"/run/user/{os.getuid()}"

# Create a named window for the rear-view camera display
cv2.namedWindow("Rear View Camera", cv2.WINDOW_NORMAL)

# Set the window size to 700x480
cv2.resizeWindow("Rear View Camera", 700, 480)

# Position the window at (0, 0)
cv2.moveWindow("Rear View Camera", 0, 0)

def draw_guide_lines(frame):
    """
    Draws parking guide lines on the frame.
    Green, yellow, and red lines represent safe, caution, and warning zones.
    """
    height, width, _ = frame.shape

    # Define zones
    safe_zone_y = int(height * 0.7)
    caution_zone_y = int(height * 0.85)
    danger_zone_y = int(height * 0.95)

    # Draw green line for the safe zone
    cv2.line(frame, (int(width * 0.2), safe_zone_y), (int(width * 0.8), safe_zone_y), (0, 255, 0), 3)

    # Draw yellow line for the caution zone
    cv2.line(frame, (int(width * 0.1), caution_zone_y), (int(width * 0.9), caution_zone_y), (0, 255, 255), 3)

    # Draw red line for the danger zone
    cv2.line(frame, (0, danger_zone_y), (width, danger_zone_y), (0, 0, 255), 3)

    # Draw diagonal white lines for guidance
    cv2.line(frame, (int(width * 0.4), safe_zone_y), (int(width * 0.3), height), (255, 255, 255), 2)
    cv2.line(frame, (int(width * 0.6), safe_zone_y), (int(width * 0.7), height), (255, 255, 255), 2)

    return frame

# Open the default webcam (index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

try:
    print("Starting rear-view camera... Press 'q' to quit.")
    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Flip the frame horizontally (mirror effect)
        frame = cv2.flip(frame, 1)

        # Add guide lines to the frame
        frame_with_lines = draw_guide_lines(frame)

        # Display the frame
        cv2.imshow("Rear View Camera", frame_with_lines)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nStopping rear-view camera...")

finally:
    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
    print("Rear-view camera stopped.")

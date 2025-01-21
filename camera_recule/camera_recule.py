import cv2
import numpy as np
from picamera2 import Picamera2

# Initialize the Picamera2
picam2 = Picamera2()
picam2.start()

# Create a named window for the rear-view camera display
cv2.namedWindow("Rear View Camera", cv2.WINDOW_NORMAL)

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

try:
    print("Starting rear-view camera... Press 'q' to quit.")
    while True:
        # Capture a frame from the camera
        frame = picam2.capture_array()

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
    # Stop the camera and close all OpenCV windows
    picam2.stop()
    cv2.destroyAllWindows()
    print("Rear-view camera stopped.")

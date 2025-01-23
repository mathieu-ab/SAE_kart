import cv2
import numpy as np
from picamera2 import Picamera2

# Initialize the camera
picam2 = Picamera2()
picam2.start()

# Create a fullscreen window without title bar
cv2.namedWindow("Rear View Camera", cv2.WND_NORMAL)
cv2.setWindowProperty("Rear View Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

def draw_guide_lines(frame):
    """
    Draws parking guide lines on the frame.
    Softer colors represent safe, caution, and warning zones.
    """
    height, width, _ = frame.shape

    # Set y coordinates for the guide lines
    safe_zone_y = int(height * 0.75)  # 75% of height
    caution_zone_y = int(height * 0.875)  # 87.5% of height
    danger_zone_y = height  # Bottom of the frame

    # Draw guide lines with natural colors
    cv2.line(frame, (int(width * 0.2), safe_zone_y), (int(width * 0.8), safe_zone_y), (144, 238, 144), 3)  # Light Green
    cv2.line(frame, (int(width * 0.1), caution_zone_y), (int(width * 0.9), caution_zone_y), (255, 255, 224), 3)  # Light Yellow
    cv2.line(frame, (0, danger_zone_y), (width, danger_zone_y), (255, 182, 193), 3)  # Light Red

    # Draw diagonal lines
    cv2.line(frame, (int(width * 0.4), safe_zone_y), (int(width * 0.3), height), (255, 255, 255), 2)
    cv2.line(frame, (int(width * 0.6), safe_zone_y), (int(width * 0.7), height), (255, 255, 255), 2)

    return frame

try:
    print("Starting rear-view camera... Press 'q' to quit.")
    while True:
        # Capture frame from the camera
        frame = picam2.capture_array()

        # Invert the frame (flip vertically)
        frame = cv2.flip(frame, 0)

        # Resize the frame to have a height of 480 pixels
        height = 480
        aspect_ratio = frame.shape[1] / frame.shape[0]
        width = int(height * aspect_ratio)
        frame_resized = cv2.resize(frame, (width, height))

        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)

        # Apply color correction (example: increase red channel)
        frame_rgb[:, :, 0] = cv2.add(frame_rgb[:, :, 0], 20)  # Increase red channel

        # Draw guide lines on the frame
        frame_with_lines = draw_guide_lines(frame_rgb)

        # Show the frame in the window
        cv2.imshow("Rear View Camera", frame_with_lines)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nStopping rear-view camera...")

finally:
    # Stop the camera and close the window
    picam2.stop()
    cv2.destroyAllWindows()
    print("Rear-view camera stopped.")

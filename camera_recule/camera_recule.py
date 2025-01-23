import cv2
import numpy as np
from picamera2 import Picamera2


picam2 = Picamera2()
picam2.start()


cv2.namedWindow("Rear View Camera", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Rear View Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


button_x, button_y, button_w, button_h = 10, 10, 200, 50
running = True

def stop_video(event, x, y, flags, param):
    global running

    if event == cv2.EVENT_LBUTTONDOWN:
        if button_x < x < button_x + button_w and button_y < y < button_y + button_h:
            print("Button clicked, stopping video stream.")
            running = False


cv2.setMouseCallback("Rear View Camera", stop_video)

def draw_guide_lines(frame):

    height, width, _ = frame.shape

    safe_zone_y = int(height * 0.7)
    caution_zone_y = int(height * 0.85)
    danger_zone_y = int(height * 0.95)


    cv2.line(frame, (int(width * 0.2), safe_zone_y), (int(width * 0.8), safe_zone_y), (0, 255, 0), 3)

    cv2.line(frame, (int(width * 0.1), caution_zone_y), (int(width * 0.9), caution_zone_y), (0, 255, 255), 3)

    cv2.line(frame, (0, danger_zone_y), (width, danger_zone_y), (0, 0, 255), 3)


    cv2.line(frame, (int(width * 0.4), safe_zone_y), (int(width * 0.3), height), (255, 255, 255), 2)
    cv2.line(frame, (int(width * 0.6), safe_zone_y), (int(width * 0.7), height), (255, 255, 255), 2)

    return frame
def video_stream():
    global running
    print("Starting rear-view camera... Press 'q' to quit.")
    while running:
        frame = picam2.capture_array()


        frame = cv2.flip(frame, 1)


        frame_with_lines = draw_guide_lines(frame)


        button_color = (0, 0, 255)  # Red button color
        cv2.rectangle(frame_with_lines, (button_x, button_y), (button_x + button_w, button_y + button_h), button_color, -1)


        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame_with_lines, "Stop", (button_x + 50, button_y + 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)


        cv2.imshow("Rear View Camera", frame_with_lines)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            running = False
            break


video_stream()


cv2.destroyAllWindows()
picam2.stop()
print("Rear-view camera stopped.")



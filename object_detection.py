from ultralytics import YOLO
import cv2

# YOLOv8n is the smallest and fastest model, but it is also the least accurate.
# For webcam detection, use a slightly larger model to reduce false labels.
model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Could not open webcam.")

# Optional: improve stability on some webcams
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not read frame from webcam.")
        break

    # Resize to a standard input size and set a stricter confidence threshold.
    # This reduces false positives from noisy webcam frames.
    results = model(frame, imgsz=640, conf=0.45, iou=0.5, verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow("AI Object Detection - Press Q to Exit", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

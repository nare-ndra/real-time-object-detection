import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time
import threading

def get_camera_index():
    for i in range(4):
        cap = cv2.VideoCapture(i)
        if cap.isOpened() and cap.read()[0]:
            cap.release()
            return i
    return None

def display_fps(frame, fps):
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def object_detection_thread(frame, results):
    # Run object detection on a separate thread
    bbox, label, conf = cv.detect_common_objects(frame)
    results["bbox"] = bbox
    results["label"] = label
    results["conf"] = conf

camera_index = get_camera_index()
if camera_index is None:
    print("No camera detected. Please make sure your camera is connected.")
    exit()

video = cv2.VideoCapture(camera_index)
if not video.isOpened():
    print("Failed to open the camera.")
    exit()

labels = []
prev_labels = set()
fps = 0
start_time = time.time()

results = {"bbox": [], "label": [], "conf": []}
detection_thread = None
frame_count = 0
detection_interval = 3  # Perform detection every 3 frames

print("Press 'q' to exit the application.")

while True:
    ret, frame = video.read()
    if not ret:
        print("Error reading frame from camera.")
        break

    # Resize the frame for faster processing
    frame_resized = cv2.resize(frame, (640, 480))

    # Run object detection every `detection_interval` frames
    if frame_count % detection_interval == 0:
        if detection_thread is None or not detection_thread.is_alive():
            detection_thread = threading.Thread(target=object_detection_thread, args=(frame_resized, results))
            detection_thread.start()

    # Draw bounding boxes if detection results are available
    if results["bbox"]:
        output_image = draw_bbox(frame_resized, results["bbox"], results["label"], results["conf"])
    else:
        output_image = frame_resized

    # Update FPS
    current_time = time.time()
    fps = 1 / (current_time - start_time)
    start_time = current_time
    display_fps(output_image, fps)

    # Show the output image
    cv2.imshow("Optimized Object Detection", output_image)
    cv2.resizeWindow("Optimized Object Detection", 800, 600)

    # Track detected labels
    new_labels = set(results["label"])
    if new_labels != prev_labels:
        print("New objects detected:", ", ".join(new_labels - prev_labels))
        prev_labels = new_labels

    frame_count += 1

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

if not prev_labels:
    print("No objects detected.")
else:
    print("Objects detected during the session:", ", ".join(prev_labels))

video.release()
cv2.destroyAllWindows()

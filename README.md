# object-detection

Here's a **README** file for your object detection project. It provides a detailed overview of the project, setup instructions, and usage guidelines.

---

# 📸 Real-Time Object Detection using OpenCV and CVLib

This project is a real-time object detection application using **OpenCV** and **CVLib**. It captures video from your camera, identifies common objects in the frame, and displays bounding boxes around them with labels and confidence scores. It uses pre-trained deep learning models, making it easy to detect a variety of objects without the need for custom training.

## 🚀 Features
- **Real-Time Object Detection** using a pre-trained YOLO model.
- **Multi-threading** for improved performance.
- **FPS Counter** for real-time performance monitoring.
- **New Object Alert**: Notifies when new objects are detected in the frame.
- **Auto Camera Detection**: Automatically identifies an active camera.

## 🛠️ Technologies Used
- **Python**
- **OpenCV**: For video capture and image processing.
- **CVLib**: Simplified object detection using YOLO.
- **YOLO (You Only Look Once)**: Pre-trained deep learning model for object detection.

## 📦 Installation

### Prerequisites
Ensure you have **Python 3.7 or above** installed.

### Install Required Packages
Run the following command to install the dependencies:

```bash
pip install opencv-python cvlib playsound gTTS
```

> **Note**: If you have a compatible GPU, consider installing the CUDA-enabled version of OpenCV for better performance:
> ```bash
> pip install opencv-python-headless
> ```

## 🚀 Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/object-detection.git
   cd object-detection
   ```

2. **Run the Script**
   ```bash
   python object_detection.py
   ```

3. **Controls**
   - Press **'q'** to exit the application.

## 📝 Example Output
When the script is running, it captures frames from the camera, detects objects, and displays them with bounding boxes and labels. It also prints alerts for newly detected objects in the terminal.

**Sample Detected Objects:**
```
New objects detected: car, person
New objects detected: person, dog
Objects detected during the session: car, person, dog
```

## 📊 Performance Tips
- **Resize Input Frames**: The input frames are resized for faster processing.
- **Multi-threading**: Object detection runs in a separate thread, improving FPS.
- **Detection Interval**: Object detection is performed every few frames to reduce computation.

## 🤖 How It Works
1. **Camera Initialization**: Automatically detects an active camera.
2. **Frame Capture**: Captures frames from the video feed in real-time.
3. **Object Detection**: Uses the `cvlib` library's `detect_common_objects()` function, which internally uses a pre-trained YOLO model.
4. **Display**: Annotates the frame with bounding boxes and labels, displaying it in a window.
5. **Alert for New Objects**: Alerts the user when new objects are detected.

## 🛠️ Customization
- To use a different model (e.g., **YOLOv4-tiny**, **YOLOv5**), replace the object detection function with a custom model integration.
- Modify the `detection_interval` parameter in the script to control the frequency of detection.

## 📚 Data Source
- The object detection is based on the **YOLO model trained on the COCO dataset**, which can identify **80 common object classes**, including:
  - Animals: `cat`, `dog`, `bird`
  - Vehicles: `car`, `bus`, `truck`
  - Everyday Objects: `bottle`, `chair`, `laptop`

## 🐞 Troubleshooting
- **Camera Not Detected**: Ensure your camera is connected and not being used by another application.
- **Low FPS**: Reduce the input frame size or increase the `detection_interval`.
- **No Objects Detected**: Ensure there is sufficient lighting for the camera to capture clear frames.


## 🙏 Acknowledgements
- [OpenCV](https://opencv.org/) for computer vision tools.
- [CVLib](https://www.cvlib.net/) for simplified object detection.
- [COCO Dataset](https://cocodataset.org/) for the pre-trained model.


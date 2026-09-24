# AI-Based Object Detection System

A real-time object detection system built using **Python, OpenCV, and YOLO**. The application detects and labels multiple objects from live camera or video input and displays bounding boxes with confidence scores.

## 🚀 Features

* Real-time object detection
* Webcam and video input support
* Multiple object detection
* Object labels and confidence scores
* Bounding box visualization
* Fast YOLO-based detection

## 🛠️ Technologies Used

* Python
* OpenCV
* YOLO
* NumPy

## 📂 Project Structure

```text
AI-Object-Detection/
│
├── object_detection.py
├── requirements.txt
├── yolov8n.pt
├── README.md
├── images/
└── results/
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/AI-Object-Detection.git
cd AI-Object-Detection
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python file:

```bash
python object_detection.py
```

The webcam will open and detect objects in real time.

Press **Q** to exit the application.

## 📸 Demo

Add screenshots or a short GIF of the object detection output in the `images` folder.

## 💡 How It Works

1. Captures frames from the webcam or video.
2. Sends each frame to the YOLO model.
3. YOLO identifies objects in the frame.
4. Bounding boxes and confidence scores are generated.
5. OpenCV displays the processed frame in real time.

## 🔮 Future Improvements

* Add object tracking
* Support custom-trained YOLO models
* Add detection counting
* Add video file upload
* Create a web-based interface

## 👨‍💻 Author

**Naveenkumar P**

GitHub: https://github.com/YOUR-USERNAME
LinkedIn: https://www.linkedin.com/

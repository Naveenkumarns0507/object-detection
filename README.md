# AI-Based Object Detection System

A real-time object detection system developed using **Python, OpenCV, and YOLO**. The application detects and labels multiple objects from a live webcam feed and displays bounding boxes with confidence scores.

## 🚀 Features

* Real-time object detection
* Webcam input support
* Detection of multiple objects
* Object labels and confidence scores
* Bounding box visualization
* YOLO-based fast detection

## 🛠️ Technologies Used

* **Python**
* **OpenCV**
* **YOLO (Ultralytics)**
* **NumPy**

## 📂 Project Structure

```text
object-detection/
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
git clone https://github.com/Naveenkumarns0507/object-detection.git
cd object-detection
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the application:

```bash
python object_detection.py
```

The webcam will open and the YOLO model will detect objects in real time.

Press **Q** to exit the application.

## 📸 Demo

Add screenshots or a GIF showing the object detection results to the `images` folder.

Example:

```text
Webcam → YOLO Model → Object Detection → Bounding Boxes + Confidence Scores
```

## 💡 How It Works

1. Captures frames from the webcam using OpenCV.
2. Sends each frame to the YOLO model.
3. YOLO detects objects present in the frame.
4. Generates bounding boxes, object labels, and confidence scores.
5. OpenCV displays the processed frame in real time.

## 🔮 Future Improvements

* Object tracking
* Object counting
* Custom-trained YOLO models
* Video file upload support
* Web-based interface

## 👨‍💻 Author

**Naveenkumar P**

GitHub: [Naveenkumarns0507](https://github.com/Naveenkumarns0507)

LinkedIn: [Naveenkumar P]([https://www.linkedin.com/](https://www.linkedin.com/in/naveenkumar-s18/))

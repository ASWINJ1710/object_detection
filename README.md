# 🔍 Live Object Detection System using YOLO-World

A real-time object detection application built using **YOLO-World, OpenCV, and Streamlit**. The system detects and identifies multiple objects through a live webcam feed using open-vocabulary object detection.

Unlike traditional object detection models that support a fixed set of classes, YOLO-World allows users to detect a wider range of objects using custom text-based class prompts.

## 🚀 Project Overview

The Live Object Detection System captures real-time video from a webcam, processes each frame using the YOLO-World model, and displays detected objects with bounding boxes, class names, and confidence scores.

The application provides an interactive Streamlit dashboard to configure object categories and detection confidence.

## ✨ Key Features

- **Real-Time Detection:** Detect objects directly through a webcam.
- **Open-Vocabulary Detection:** Identify objects using custom text prompts.
- **300+ Object Prompts:** Includes a large vocabulary across 17 object categories.
- **Bounding Box Visualization:** Displays detected objects with bounding boxes.
- **Confidence Scores:** Shows the confidence score for each detection.
- **Object Counting:** Displays the number of detected instances for each class.
- **Interactive Dashboard:** Configure detection settings through Streamlit.
- **Adjustable Confidence:** Control the detection confidence threshold.
- **Multiple Object Categories:** Detect objects from different environments.

## 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| YOLO-World | Open-vocabulary object detection |
| OpenCV | Webcam access and image processing |
| Streamlit | Interactive web interface |
| PyTorch | Deep learning framework |
| Ultralytics | YOLO-World model implementation |

## 🏗️ System Architecture

```text
        Webcam Input
             |
             v
      OpenCV Video Capture
             |
             v
       Frame Processing
             |
             v
       YOLO-World Model
             |
             v
     Object Classification
       and Localization
             |
             v
      Bounding Box Drawing
             |
             v
     Confidence and Counting
             |
             v
       Streamlit Dashboard
             |
             v
       Real-Time Output
```

## 📂 Project Structure

```text
Live_Object_Detection/
│
├── app.py                 # Streamlit application
├── detector.py            # YOLO-World detection logic
├── classes.py             # Object categories and prompts
├── requirements.txt       # Project dependencies
├── .gitignore             # Git ignored files
│
├── models/                # Optional local model storage
├── assets/                # Project images and screenshots
│
└── README.md
```

Model weights and downloaded runtime files are excluded from GitHub because of their large file sizes.

## 📦 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ASWINJ1710/object_detection.git
```

### 2. Navigate to the Project Folder

```bash
cd object_detection
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🎯 Object Detection Categories

The application includes 17 categories with approximately 300 unique object prompts.

1. Electronics
2. Home Appliances
3. Vehicles
4. Animals
5. Office and Stationery
6. Food and Groceries
7. Tools
8. Sports Equipment
9. Personal Accessories
10. Household Objects
11. Toys and Games
12. Musical Instruments
13. Medical Equipment
14. Construction Objects
15. Plants and Gardening
16. Insects
17. Industrial and Workshop Objects

## ⚙️ Model Information

**Model:** YOLO-World Small (YOLOv8s-Worldv2)

YOLO-World is an open-vocabulary object detection model designed to detect objects using text descriptions.

The model uses visual and language representations to associate image regions with text-based object categories.

**Important:** Model weights are not included in this repository. The Ultralytics implementation downloads required weights when they are not available locally. An internet connection may be required during the first run.

## 💡 Applications

- Smart surveillance systems
- Real-time object monitoring
- Educational computer vision projects
- Retail object identification
- Industrial object detection
- Smart home applications
- General-purpose visual detection

## ⚠️ Limitations

- Detection accuracy depends on lighting, camera quality, and object visibility.
- Small or heavily occluded objects may not be detected correctly.
- Processing speed depends on available hardware.
- Open-vocabulary detection does not guarantee recognition of every possible object.
- Webcam access is required for live detection.

## 🔮 Future Improvements

- Object tracking with unique tracking IDs.
- Detection history and analytics dashboard.
- Video file upload and processing.
- Object detection alerts.
- GPU acceleration.
- Export detection reports.
- Custom object category management.

## 👨‍💻 Author

**Aswin J**

GitHub: [@ASWINJ1710](https://github.com/ASWINJ1710)

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

**Built with Python, OpenCV, YOLO-World, and Streamlit.**

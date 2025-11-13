<div align="center">

# 🧍‍♂️ Real-Time Human Detection using MobileNet-SSD (DNN)

A high-performance, real-time human detection system using  
**MobileNet-SSD (Deep Neural Network)** + **Object Tracking**, supporting  
**Image detection, Video detection, and Live Camera detection**.

![Demo](https://user-images.githubusercontent.com/000000/placeholder.gif)

</div>

---

## 🚀 Features

- ✔ **Deep Learning Human Detection** using MobileNet-SSD (DNN)
- ✔ **Real-time Performance** with frame-skipping optimization
- ✔ **Multi-Object Tracking** (KCF / CSRT / MIL fallback)
- ✔ Supports:
  - 📷 **Camera Detection**
  - 🎞️ **Video File Detection**
  - 🖼️ **Image File Detection**
- ✔ **Non-blocking threaded capture**
- ✔ **FPS Optimization**
- ✔ Easy-to-use **interactive menu**
- ✔ Works on CPU (GPU optional)

---
## 🧠 How It Works

### 🔹 Step 1 — DNN Detection (MobileNet-SSD)
Runs the MobileNet-SSD network every **N frames** (`DETECTION_INTERVAL`)  
to detect all people in the scene.

### 🔹 Step 2 — Object Tracking (KCF / CSRT / MIL)
Between DNN detections, an object tracker:
- follows each person
- preserves IDs  
- improves FPS  
- reduces computation cost  

### 🔹 Step 3 — Automatic Tracker Switching  
If a tracker is missing from your OpenCV build, system:
- checks for **non-legacy** API
- checks for `cv2.legacy`
- falls back to **MIL** tracker

This prevents crashes and keeps the system stable on all OpenCV versions.

---

## 📦 Installation

### **1️⃣ Install dependencies**
```bash
pip install opencv-python imutils numpy
pip install opencv-contrib-python (optional)
```
## 🔽 Download Required DNN Files

Download and place the following files inside the **`models/`** folder:

| File Name                         | Description           |
|----------------------------------|-----------------------|
| `MobileNetSSD_deploy.prototxt`   | Network architecture  |
| `MobileNetSSD_deploy.caffemodel` | Pre-trained weights   |

## ▶️ Menu Preview

You will see a menu:

=== Real-Time Human Detection Model ===
- Camera
- Video file path
- Image file path
- Exit
---
## 📝 Usage Examples

### 🎥 Detect from video
Enter video path: D:\videos\street.mp4

### 📷 Detect from camera
Enter choice: 1

### 🖼️ Detect from image
Enter image path: images/test1.jpg
---
## 🛠️ Future Improvements

- 🚶 Upgrade to YOLOv8 for high-accuracy pedestrian detection  
- 🧠 Add SORT/DeepSORT tracking  
- 🗂️ Multi-class detection (cars, bikes, bags, etc.)  
- 📊 FPS & latency monitor  
- 🖥️ GUI (Tkinter / PyQt)  
---
## 🤝 Contributing
Pull requests are welcome!  
Feel free to open issues, request features, or suggest improvements.
---
<div align="center">

⭐ If you like this project, give it a star on GitHub!

</div>



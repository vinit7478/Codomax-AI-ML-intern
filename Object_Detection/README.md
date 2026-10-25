# YOLOv8 Object Detection

## 📌 About
This project uses the pretrained YOLOv8m model to detect multiple objects using a webcam, image, or video with Python.

## 🛠️ Installation

```bash
pip install ultralytics opencv-python
```

## 💻 Webcam Detection

```python
from ultralytics import YOLO

model = YOLO('yolov8m.pt')
model(source=0, show=True, conf=0.4, device="cpu", save=True)
```

## 🖼️ Image Detection

Place your image inside the `images` folder and use:

```python
model(source='images/test.jpg', show=True, conf=0.4, device="cpu", save=True)
```

## 🎥 Video Detection

Place your video inside the `videos` folder and use:

```python
model(source='videos/test.mp4', show=True, conf=0.4, device="cpu", save=True)
```

## 📁 Output
Detection results are saved automatically in the `runs/detect/` folder.

**Note:** The `yolov8m.pt` model downloads automatically if it is not available locally.

## 👨‍💻 Technologies
- Python
- YOLOv8
- OpenCV
- Ultralytics



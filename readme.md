# 🐾 AI-Powered Smart Wildlife Monitoring System

An advanced AI-based wildlife detection and monitoring web application built using **Flask** and **YOLOv8**.

This system can:
- detect animals from uploaded images
- display confidence scores
- draw bounding boxes
- provide animal information
- support real-time monitoring

---

# 🚀 Features

## 🔍 AI Animal Detection
- YOLOv8 animal detection
- Bounding box visualization
- Confidence score prediction
- Multi-animal detection support

## 🧠 Smart Wildlife Information
- Scientific names
- Habitat information
- Conservation status
- Dangerous animal alerts

## 📊 Analytics Dashboard
- Detection history
- Detection statistics
- AI monitoring interface

## 🎥 Real-Time Detection
- Webcam live detection
- Video upload support

## 🎨 Modern UI/UX
- Futuristic AI dashboard
- Responsive layout
- Interactive animations

---

# 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend |
| Flask | Web Framework |
| YOLOv8 | AI Object Detection |
| OpenCV | Image & Video Processing |
| SQLite | Database |
| HTML/CSS | Frontend |

---

# 📂 Project Structure

```text
project/
│
├── app.py
├── animal_info.py
├── requirements.txt
├── yolov8n.pt
├── database.db
│
├── static/
│   ├── style.css
│   ├── uploads/
│   ├── results/
│   └── videos/
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── webcam.html
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Download YOLOv8 Model

Download:

`yolov8n.pt`

Official model:

https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8n.pt

Place it inside the project folder.

---

# ▶️ Run the Project

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# 🧠 How It Works

```text
Image Upload
      ↓
YOLOv8 Detects Animals
      ↓
Bounding Boxes Generated
      ↓
Confidence Scores Calculated
      ↓
Animal Information Retrieved
      ↓
Results Displayed on Dashboard
```

---

# 📸 Screenshots

- Main Dashboard
- Detection Preview
- Analytics Dashboard
- Live Webcam Detection

---

# 🧪 Future Improvements

- Custom wildlife dataset training
- Rare species detection
- GPS wildlife tracking
- Email alerts
- Admin dashboard
- Cloud deployment

---

# 📚 AI Model

This project uses:
- YOLOv8 Nano (`yolov8n.pt`)
- Ultralytics Framework

Official Website:
https://ultralytics.com/

---

# 👨‍💻 Author

Anirudh Kapoor

🐾 AI-Powered Smart Wildlife Monitoring System
An advanced AI-based wildlife detection and monitoring web application built using Flask and YOLOv8.
This system can detect animals from uploaded images, display confidence scores, draw bounding boxes, provide animal information, and support real-time monitoring features.

🚀 Features
🔍 AI Animal Detection


Detect animals using YOLOv8


Bounding box visualization


Confidence score prediction


Multi-animal detection support


🧠 Smart Wildlife Information


Scientific names


Habitat information


Conservation status


Dangerous animal alerts


📊 Analytics Dashboard


Detection history


Detection statistics


AI monitoring interface


🎥 Real-Time Detection


Webcam live detection


Video upload support


🎨 Modern UI/UX


Futuristic AI dashboard


Glassmorphism design


Responsive layout


Interactive animations



🛠️ Tech Stack
TechnologyUsagePythonBackendFlaskWeb FrameworkYOLOv8AI Object DetectionOpenCVImage & Video ProcessingSQLiteDetection DatabaseHTML/CSSFrontendJavaScriptFrontend Interactions

📂 Project Structure
project/│├── app.py├── animal_info.py├── requirements.txt├── yolov8n.pt├── database.db│├── static/│   ├── style.css│   ├── uploads/│   ├── results/│   └── videos/│├── templates/│   ├── index.html│   ├── dashboard.html│   └── webcam.html│└── README.md

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/your-repository.gitcd your-repository

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Download YOLOv8 Model
Download:


yolov8n.pt


Official Model:
https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov8n.pt
Place it inside the project folder.

▶️ Run the Project
python app.py
Open browser:
http://127.0.0.1:5000

🧠 How It Works
Image Upload      ↓YOLOv8 Detects Animals      ↓Bounding Boxes Generated      ↓Confidence Scores Calculated      ↓Animal Information Retrieved      ↓Results Displayed on Dashboard

📸 Screenshots
Main Dashboard


AI-powered wildlife detection interface


Image upload system


Detection preview


Detection Results


Bounding boxes


Confidence scores


Animal information cards


Analytics Dashboard


Detection history


Monitoring system



🐾 Supported Animals
Current default YOLOv8 classes include:


Dog


Cat


Horse


Elephant


Bear


Zebra


Giraffe



⚠️ Important Note
The default YOLOv8 COCO model does not support some wildlife classes like:


Lion


Tiger


Leopard


To detect custom wildlife species, a custom-trained YOLOv8 model is required.

🧪 Future Improvements


Custom wildlife dataset training


Rare species detection


GPS wildlife tracking


Email/SMS alerts


Admin dashboard


Cloud deployment


Mobile app support


Heatmap analytics



📚 AI Model
This project uses:


YOLOv8 Nano (yolov8n.pt)


Ultralytics framework


Official Website:
https://ultralytics.com/

👨‍💻 Author
Developed by:
Anirudh Kapoor


⭐ Acknowledgements


Ultralytics YOLOv8


Flask Framework


OpenCV


Roboflow


Kaggle Datasets
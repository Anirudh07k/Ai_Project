from flask import Flask, render_template, request, Response
from ultralytics import YOLO
from PIL import Image
import cv2
import os
import sqlite3
from datetime import datetime
from animal_info import animal_data

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"
VIDEO_FOLDER = "static/videos"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)
os.makedirs(VIDEO_FOLDER, exist_ok=True)

model = YOLO("yolov8n.pt")

# =========================
# DATABASE SETUP
# =========================

def init_db():
    conn = sqlite3.connect("database.db")

    conn.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal TEXT,
            confidence REAL,
            image TEXT,
            time TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

# =========================
# SAVE DETECTIONS
# =========================

def save_detection(animal, confidence, image):
    conn = sqlite3.connect("database.db")

    conn.execute(
        "INSERT INTO detections (animal, confidence, image, time) VALUES (?, ?, ?, ?)",
        (
            animal,
            confidence,
            image,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()
    conn.close()

# =========================
# IMAGE DETECTION
# =========================

def detect_image(image_path):

    # Read image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        raise Exception(
            "Invalid image format. Please upload JPG or PNG."
        )

    results = model(image)

    result = results[0]

    annotated_frame = result.plot()

    output_path = os.path.join(
        RESULT_FOLDER,
        "result.jpg"
    )

    cv2.imwrite(output_path, annotated_frame)

    detections = []

    boxes = result.boxes

    for box in boxes:

        cls_id = int(box.cls[0])

        confidence = float(box.conf[0])

        label = model.names[cls_id]

        save_detection(
            label,
            round(confidence * 100, 2),
            output_path
        )

        info = animal_data.get(label.lower(), {})

        detections.append({
            "name": label,
            "confidence": round(confidence * 100, 2),
            "scientific": info.get(
                "scientific",
                "Unknown"
            ),
            "habitat": info.get(
                "habitat",
                "Unknown"
            ),
            "status": info.get(
                "status",
                "Unknown"
            )
        })

    return detections, output_path

# =========================
# HOME PAGE
# =========================

# Allowed image formats
ALLOWED_EXTENSIONS = {
    'png',
    'jpg',
    'jpeg'
}

@app.route("/", methods=["GET", "POST"])
def index():

    detections = []
    image_path = None

    if request.method == "POST":

        file = request.files["image"]

        if file:

            # Convert filename to lowercase
            filename = file.filename.lower()

            # Validate extension
            if not filename.endswith(
                ('.png', '.jpg', '.jpeg')
            ):
                return "Only JPG and PNG supported"

            # Save image
            path = os.path.join(
                UPLOAD_FOLDER,
                filename
            )

            file.save(path)

            # Run detection
            detections, image_path = detect_image(path)

    return render_template(
        "index.html",
        detections=detections,
        image_path=image_path
    )

# =========================
# DASHBOARD
# =========================

@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("database.db")

    data = conn.execute(
        "SELECT * FROM detections ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        data=data
    )

# =========================
# WEBCAM DETECTION
# =========================

def generate_frames():

    camera = cv2.VideoCapture(0)

    while True:

        success, frame = camera.read()

        if not success:
            break

        results = model(frame)

        annotated = results[0].plot()

        ret, buffer = cv2.imencode('.jpg', annotated)

        frame = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame +
            b'\r\n'
        )

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')

@app.route('/video_feed')
def video_feed():
    return Response(
        generate_frames(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

# =========================
# VIDEO DETECTION
# =========================

@app.route('/video', methods=['GET', 'POST'])
def video_detection():

    if request.method == 'POST':

        file = request.files['video']

        path = os.path.join(VIDEO_FOLDER, file.filename)

        file.save(path)

        return "Video uploaded successfully"

    return '''
    <h1>Upload Video</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="video">
        <button type="submit">Upload</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
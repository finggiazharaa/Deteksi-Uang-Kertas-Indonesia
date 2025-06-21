
from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO('weights/best.pt')  # path ke model hasil training

camera = cv2.VideoCapture(0)  # gunakan webcam default

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            results = model.predict(source=frame, conf=0.5, save=False)
            annotated_frame = results[0].plot()

            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)

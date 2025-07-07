💵 Indonesian Banknote Denomination Detection System Using YOLOv8

A smart web-based image recognition system designed to detect and classify the denominations on Indonesian banknotes using the YOLOv8 object detection model. This system helps in real-time identification of currency denominations from user-submitted images, supporting automation in financial verification and cash handling processes.

🧱 Background

Identifying currency denominations accurately is crucial for various applications such as banking automation, cashier systems, counterfeit detection, and inclusive technologies for the visually impaired. Manual recognition can be prone to error, especially in poor lighting or when notes are worn. By integrating a deep learning-based model, this project aims to automate the detection and classification of Indonesian banknotes with high precision.

🎯 Objectives

✅ Build and train a YOLOv8 model to detect and classify banknote denominations
✅ Create a user-friendly web interface for uploading and analyzing images
✅ Provide instant and accurate denomination feedback to users
✅ Support cash handling automation and financial technology innovations

📂 Dataset Information

🧪 Indonesian Banknote Detection Dataset
Source: Roboflow Universe – Indonesian Banknotes
Classes: Various denominations of Indonesian Rupiah (e.g., 1K, 2K, 5K, 10K, 20K, 50K, 100K)
Images: Several hundred high-quality annotated banknote images
Format: YOLOv8-compatible bounding boxes

⚙️ Implementation Process
Dataset Preparation – Annotated using Roboflow platform and exported in YOLOv8 format

Model Training – YOLOv8 used to train a robust denomination detection model

Web Development – Flask is used to create a lightweight web interface

Model Integration – The system loads the trained YOLOv8 model and processes uploaded images

Visualization – Results are displayed with bounding boxes and confidence scores

🚀 How to Use the System (Web-Based)
📦 1. Install Required Packages
bash
Copy
Edit
pip install flask ultralytics opencv-python roboflow numpy
🛠️ 2. Add the Trained Model
Place your trained YOLOv8 weights file at:

bash
Copy
Edit
weights/best.pt  # Model trained on Indonesian banknote dataset
🖥️ 3. Run the Web Application
bash
Copy
Edit
python app.py
Open your browser and visit:

arduino
Copy
Edit
http://localhost:5000/
🧪 4. Use the Interface
Upload an image of a banknote

View predicted denomination with bounding box and confidence score

📊 Model Performance
Metric	Value
Precision	Coming Soon
Recall	Coming Soon
mAP@0.5	Coming Soon
mAP@0.5:0.95	Coming Soon
Fitness Score	Coming Soon

Model performance values will be updated after final training evaluation.

Detection Demo
🖼️ Image Prediction Demo
![image](https://github.com/user-attachments/assets/2eec13d0-9624-4706-8e5c-b50b5f50e469)


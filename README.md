Deep Learning Fundus Image Analysis for Diabetic Retinopathy

This project implements an end-to-end deep learning application for early detection of Diabetic Retinopathy (DR) using retinal fundus images. A pre-trained Xception CNN is fine-tuned using transfer learning and deployed via a Flask web application to perform real-time severity classification.

⚠️ Disclaimer: This project is for educational and research purposes only and must not be used for clinical diagnosis.

📌 Features

Multi-class classification of Diabetic Retinopathy:

No DR

Mild DR

Moderate DR

Severe DR

Proliferative DR

Transfer learning using Xception (ImageNet weights)

Real-time inference through a Flask web interface

Secure image upload with validation

Model evaluation with accuracy, confusion matrix, and classification report

Clean project structure and reproducible setup

🧠 Tech Stack

Python 3.10

TensorFlow / Keras

Flask

NumPy, Pandas

HTML, CSS, JavaScript

📁 Project Structure
fundus-dr-app/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── models/
│   └── xception_dr.h5
├── ml/
│   ├── train_xception.ipynb
│   ├── evaluate.ipynb
│   └── preprocessing.py
├── data/
│   ├── training/
│   └── testing/
├── static/
│   ├── css/style.css
│   ├── images/
│   └── js/main.js
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── prediction.html
│   └── logout.html
├── uploads/
└── logs/

⚙️ Setup Instructions
1. Create Virtual Environment (Python 3.10)
python -m venv venv
venv\Scripts\activate

2. Install Dependencies
pip install -r requirements.txt

3. Add Trained Model
Place your trained model here:
models/xception_dr.h5

4. Run the Web App
python app.py

Open in browser:
http://127.0.0.1:5000

🧪 Training & Evaluation (Offline)

Train model:
ml/train_xception.ipynb

Evaluate model:
ml/evaluate.ipynb

Ensure your dataset is placed under:
data/training/
data/testing/

🔍 Inference Workflow

Login (demo session-based auth)

Upload fundus image (JPG/PNG)

Model performs preprocessing + prediction

Predicted DR severity is displayed on UI

❗ Common Issues

TensorFlow installation error
→ Use Python 3.10 only

Images not showing in UI
→ Ensure files are in static/images/ and paths use url_for('static', ...)

Model not loading
→ Check config.py model path

🚀 Future Enhancements

Add Grad-CAM for explainability

Show prediction confidence scores

Handle class imbalance during training

Deploy on cloud (Docker / Render / EC2)

Add REST API for external integration

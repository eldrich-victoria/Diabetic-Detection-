import os
import uuid
import logging
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session, flash
from logging.handlers import RotatingFileHandler
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input
from config import MODEL_PATH, UPLOAD_FOLDER, LOG_FOLDER, SECRET_KEY, IMAGE_SIZE

# ------------------ App Setup ------------------
app = Flask(__name__)
app.secret_key = SECRET_KEY

# ------------------ Logging Setup --------------
log_path = os.path.join(LOG_FOLDER, "app.log")
handler = RotatingFileHandler(log_path, maxBytes=5_000_000, backupCount=3)
logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)
logger.info("Application started")

# ------------------ Load Model -----------------
model = load_model(MODEL_PATH)

# ------------------ Routes ---------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    # Optional demo-only login page
    return render_template("login.html")

@app.route("/afterlogin", methods=["POST"])
def afterlogin():
    # Demo-only: accept any non-empty credentials
    email = request.form.get("email")
    password = request.form.get("password")
    if email and password:
        session["user"] = email
        logger.info("User logged in (demo): %s", email)
        return redirect(url_for("prediction"))
    flash("Invalid credentials.")
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    user = session.pop("user", None)
    logger.info("User logged out: %s", user)
    return render_template("logout.html")

@app.route("/prediction")
def prediction():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("prediction.html")

@app.route("/result", methods=["POST"])
def result():
    if "user" not in session:
        return redirect(url_for("login"))

    if "image" not in request.files:
        flash("No file part")
        return redirect(url_for("prediction"))

    file = request.files["image"]
    if file.filename == "":
        flash("No selected file")
        return redirect(url_for("prediction"))

    # Save uploaded file
    filename = str(uuid.uuid4()) + "_" + file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Preprocess and predict
    img = image.load_img(filepath, target_size=IMAGE_SIZE)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    pred_class = int(np.argmax(preds, axis=1)[0])

    classes = [
        "No Diabetic Retinopathy",
        "Mild DR",
        "Moderate DR",
        "Severe DR",
        "Proliferative DR"
    ]

    result_label = classes[pred_class]
    logger.info("Prediction: %s | User: %s", result_label, session.get("user"))

    return render_template("prediction.html", prediction=result_label)

# ------------------ Main -----------------------
if __name__ == "__main__":
    app.run(debug=False)

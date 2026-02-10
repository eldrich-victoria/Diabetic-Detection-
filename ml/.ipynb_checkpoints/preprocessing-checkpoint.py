import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.xception import preprocess_input

def load_and_preprocess_image(img_path, target_size=(299, 299)):
    """
    Loads an image from disk and preprocesses it for Xception model.
    Returns a numpy array of shape (1, 299, 299, 3).
    """
    if not os.path.exists(img_path):
        raise FileNotFoundError("Image path does not exist: " + img_path)

    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

def preprocess_batch(image_paths, target_size=(299, 299)):
    """
    Preprocess multiple images at once.
    image_paths: list of file paths
    Returns: numpy array of shape (N, 299, 299, 3)
    """
    batch = []
    for p in image_paths:
        arr = load_and_preprocess_image(p, target_size)
        batch.append(arr[0])
    return np.array(batch)

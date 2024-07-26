import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2
import numpy as np


model = load_model('weed_detection_model.h5')

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))  # Resize to model input size
    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def predict_weed(image_path):
    image = preprocess_image(image_path)
    prediction = model.predict(image)
    class_id = np.argmax(prediction, axis=1)
    return class_id[0]


image_path = 'path_to_image.jpg'
class_id = predict_weed(image_path)
print(f'Class ID: {class_id}')

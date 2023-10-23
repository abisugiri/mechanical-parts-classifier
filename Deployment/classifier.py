# Import library
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle
import json
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input

# Load trained model
model = load_model('cnn_model.h5', compile=False)
# Define class labels
class_labels = ['bolt', 'locatingpin', 'nut', 'washer']
  
def predict_and_display(uploaded_file, model, class_labels):
    img = Image.open(uploaded_file)
    img = img.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class_label = class_labels[predicted_class_index]

    st.image(img, use_column_width=True)
    st.write(f"Predicted Mechanical Part: {predicted_class_label}")

def run():
    st.write('##### Form Mechanical Parts Classifyer')
    # Making Form
    # Create a Streamlit form
    with st.form(key='Form Mechanical Parts Classifyer'):
        # Add a file uploader to the form
        uploaded_files = st.file_uploader("Upload a file of one of these format .JPEG/.JPG/.PNG file", accept_multiple_files=True)

        # Check if any file is uploaded
        if uploaded_files:
            for uploaded_file in uploaded_files:
                st.write("filename:", uploaded_file.name)
        # Close the form
        submitted = st.form_submit_button('Predict')
    
    if submitted:
        for uploaded_file in uploaded_files:
            # Use the predict_and_display function with the uploaded image data
            predict_and_display(uploaded_file, model, class_labels)

        
if __name__ == '__main__':
    run()
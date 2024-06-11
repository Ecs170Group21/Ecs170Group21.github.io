from flask import Flask, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from scipy.io import loadmat
import scipy.io as sio
import h5py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import random
from keras.utils import Sequence
from keras import models as Model
from keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D


UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'mat'}
MODEL_PATH = 'base_classifier/'
ALL_LABELS = {0: 'Meningioma', 1: 'Glioma', 2: 'Pituitary tumor'}

app = Flask(__name__, template_folder='docs', static_folder='docs', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model
def load_keras_model():
    model = Model.load_model(MODEL_PATH)
    return model

# Load the model when the app starts
model = load_keras_model()

# Set index as the first loaded page
@app.route('/')
def index():
    return render_template('index.html')

# Return true if file is in format "name.mat"
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Sets application page as home page for redirection
@app.route('/application')
def application():
    return render_template('application.html')

# Handle the form that was sent to the server
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'image' not in request.files:
        return redirect(url_for('application'))  # If not, redirect to application page
    # Get the file
    file = request.files['image']
    # If no file selected, redirect to application page
    if file.filename == '':
        return redirect(url_for('application'))
    # If file selected and allowed format
    if file and allowed_file(file.filename):
        # Save the file securely
        filename = secure_filename(file.filename)
        # Save the file to the uploads folder
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # Save the file to the filepath
        file.save(filepath)
        # Process the image with model
        result = process_image(filepath)
        # Render template of result.html with result in {{ result }}
        return render_template('result.html', result=result)
    return redirect(url_for('application'))

def process_image(image_path):
    # Load and process the .mat v7.3 file using h5py
    with h5py.File(image_path, 'r') as f:
        # Convert the HDF5 file to a .mat file
        mat_data = {}
        def recursively_add_keys(group, dict_obj):
            for key in group.keys():
                item = group[key]
                if isinstance(item, h5py.Dataset):
                    dict_obj[key] = item[()]
                elif isinstance(item, h5py.Group):
                    dict_obj[key] = {}
                    recursively_add_keys(item, dict_obj[key])
        
        recursively_add_keys(f, mat_data)
        
        mat_filepath = image_path.replace('.h5', '.mat')
        sio.savemat(mat_filepath, mat_data)
        print(f"HDF5 to .mat conversion complete. Saved at {mat_filepath}")
        # Load the .mat file
        mat_file = sio.loadmat(mat_filepath)
        print("Structure of the .mat file:")
        for key in mat_file.keys():
            print(f"Key: {key}, Type: {type(mat_file[key])}")
        data = preprocess(mat_file)
    # further processing...
    prediction = model_inference(data)
    return f'Prediction: {ALL_LABELS[prediction]}'

def preprocess(data):
    cjdata = data['cjdata']
    
    if 'image' not in cjdata.dtype.names:
        raise KeyError("Object 'image' not found in the 'cjdata' structure")
    
    # Accessing the image data within the cjdata structure
    datum = np.array(cjdata['image'][0,0])
    processed_data = datum / 12728  # Example normalization
    processed_data = np.expand_dims(processed_data, axis=(0,-1))

    return processed_data

def model_inference(data):
    # Convert data to the format expected by the model and run inference
    predictions = model.predict(data)
    prediction = np.argmax(predictions) + 1
    return prediction

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
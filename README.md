### README for Brain Tumor Classification Application

---

# Brain Tumor Classification Application

This repository contains the code and resources for a web-based application designed to classify brain MRI scans and identify the type of brain tumor present in the image. The application uses a convolutional neural network (CNN) to distinguish between Meningioma, Glioma, and Pituitary tumors.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Frontend](#frontend)
- [Results](#results)

## Project Description

The goal of this project is to create a neural network capable of classifying brain MRI scans to identify the type of brain tumor. By leveraging convolutional neural networks (CNNs) and various image processing techniques, we aim to contribute to the field of medical diagnostics and enhance the efficiency of tumor classification.

## Features

- Web-based interface for uploading MRI scans
- Real-time classification of brain tumors into three categories: Meningioma, Glioma, and Pituitary tumor
- Detailed result page with tumor type and confidence score
- Conversion of HDF5 files to .mat format for compatibility

## Installation

### Prerequisites

- Python 3.6+
- Flask
- Keras
- TensorFlow
- h5py
- scipy
- numpy
- matplotlib
- opencv-python

### Clone the Repository

```bash
git clone https://github.com/yourusername/brain-tumor-classification.git
cd brain-tumor-classification
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Usage
1. **Run the Application**

    ```bash
    python app.py
    ```

2. **Open Your Browser**

    Navigate to `http://localhost:5000` to access the application.

3. **Upload an MRI Scan**

    Upload a `.mat` file containing the MRI scan. The application will process the file and display the classification results.

### File Descriptions
- `app.py`: Contains the Flask web application code, handles file uploads, model loading, and prediction.
- `classification.py`: Implements the convolutional neural network for classifying MRI scans.
- `templates/`: Contains HTML templates for the web application.
- `static/`: Contains static files like CSS and JavaScript.
- `uploads/`: Directory where uploaded MRI scans are temporarily stored.

### Frontend
A demo of the frontend is shown below.


https://github.com/Ecs170Group21/Ecs170Group21.github.io/assets/57011512/8464e8a1-6fde-4dd6-8831-73fdddda2784



### Results
The convolutional neural network achieves high accuracy in classifying brain tumors. Detailed results, including precision, recall, and F1-score for each class, can be found in the final project report.



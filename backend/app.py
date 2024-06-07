# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)
    
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import predict  # Import your model loading and prediction functions here

app = Flask(__name__)
CORS(app)  # Enable CORS if you need cross-origin requests from your frontend

@app.route('/predict', methods=['POST'])
def predict():
    # Assume an image file is sent in the request
    image = request.files['file']
    # Process the image with your CNN
    prediction = predict(image)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)


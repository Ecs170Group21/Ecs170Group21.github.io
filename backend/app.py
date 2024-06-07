from flask import Flask, send_from_directory
import os
app = Flask(__name__, static_folder='../docs', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../docs', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable set by Heroku
    app.run(debug=False, host='0.0.0.0', port=port) 
    
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from model import predict  # Import your model loading and prediction functions here

# app = Flask(__name__)
# CORS(app)  # Enable CORS if you need cross-origin requests from your frontend

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Assume an image file is sent in the request
#     image = request.files['file']
#     # Process the image with your CNN
#     prediction = predict(image)
#     return jsonify({'prediction': prediction})

# if __name__ == '__main__':
#     app.run(debug=True)


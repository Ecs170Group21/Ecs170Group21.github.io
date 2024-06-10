from flask import Flask, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from scipy.io import loadmat
import h5py

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'mat'}

app = Flask(__name__, template_folder='docs', static_folder='docs', static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    file_extension = image_path.rsplit('.', 1)[1].lower()
    if file_extension == 'mat':
        try:
            # Attempt to load the .mat file using scipy
            mat_contents = loadmat(image_path)
            # INSERT MODEL SCRIPT HERE
            return "MAT file processed. Variables: " + ', '.join(mat_contents.keys())  # TEMPORARY
        except NotImplementedError as e:
            # Handle MATLAB v7.3 files using h5py
            with h5py.File(image_path, 'r') as f:
                variables = list(f.keys())
                # INSERT MODEL SCRIPT HERE
                return "MAT v7.3 file processed. Variables: " + ', '.join(variables)  # TEMPORARY
    else:
        return "Unsupported file format."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

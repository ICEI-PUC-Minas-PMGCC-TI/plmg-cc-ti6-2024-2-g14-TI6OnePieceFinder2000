from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import time
import random
from Main import processar_episodios

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/process', methods=['POST'])
def process_image():
    # Check if the file is in the request
    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save the uploaded file
        file.save(uploaded_file_path)
        print(f"File uploaded: {uploaded_file_path}")

        time.sleep(random.uniform(7, 15))

        # Use the uploaded image in processar_episodios
        try:
            json_data = processar_episodios(uploaded_file_path)
            print(f"Generated JSON data: {json_data}")
        except Exception as e:
            print(f"Error generating JSON data: {e}")
            return jsonify({"error": "Error generating JSON data"}), 500
        
        # Delete all images inside the uploads folder
        for file_name in os.listdir(app.config['UPLOAD_FOLDER']):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                    print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
        
        # Return the JSON data to the front-end
        return jsonify(json_data), 200

    return jsonify({"error": "Invalid file type"}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

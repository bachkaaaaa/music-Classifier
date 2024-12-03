from flask import Flask, request, jsonify
from flask_cors import CORS

import librosa
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["http://localhost:1002"])  # Enable CORS for Angular's port

app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load the VGG19 model
model_path = 'vgg19_genre_classifier.h5'
model = load_model(model_path)

# Genres list (ensure it matches the training labels)
genres = ["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"]

# Define the function to predict genre
def predict_genre(file_path, model):
    hop_length = 512
    n_fft = 2048
    n_mels = 128

    # Load and preprocess the audio file
    signal, rate = librosa.load(file_path, sr=22050)  # Match model training sample rate
    S = librosa.feature.melspectrogram(y=signal, sr=rate, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
    S_DB = librosa.power_to_db(S, ref=np.max)

    # Resize the mel spectrogram to match the VGG19 input shape
    img_height, img_width = 224, 224  # VGG19 standard input size
    S_DB_resized = tf.image.resize(S_DB, (img_height, img_width))
    S_DB_resized = S_DB_resized.numpy()  # Convert to NumPy array if needed

    # Add batch and channel dimensions (VGG19 expects 4D input: batch, height, width, channels)
    S_DB_input = np.expand_dims(S_DB_resized, axis=0)  # Add batch dimension
    S_DB_input = np.expand_dims(S_DB_input, axis=-1)  # Add channel dimension (1 for grayscale)

    # Predict the genre
    predictions = model.predict(S_DB_input)
    genre_index = np.argmax(predictions)
    return genres[genre_index]

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Check if a file is uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    # Save the file to the upload folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Predict the genre
    try:
        predicted_genre = predict_genre(filepath, model)
        result = {'genre': predicted_genre}
    except Exception as e:
        result = {'error': str(e)}

    # Clean up uploaded file
    os.remove(filepath)

    return jsonify(result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

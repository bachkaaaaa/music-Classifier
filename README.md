# Music Genre Classification

This project aims to classify music tracks based on their genres using machine learning models: VGG (Convolutional Neural Network) and SVM (Support Vector Machine). The project is built with **Flask** for the backend API and **Angular** for the frontend interface.

## Features

- **Music Genre Classification**: Classify music tracks into predefined genres using VGG and SVM models.
- **Upload Audio**: Users can upload an audio file, and the backend will classify the genre using the trained models.
- **Results Display**: The classified genre is shown to the user on the frontend along with the confidence score of the classification.
- **Model Selection**: Users can choose between two models, VGG and SVM, for classification.
- **Real-Time Feedback**: Display real-time feedback and loading indicators while the model processes the music.

## Technologies Used

- **Flask**: A Python web framework to create the backend API that handles audio classification requests.
- **Angular**: A frontend framework to build a dynamic, single-page application (SPA) for interacting with the user.
- **VGG Model**: A pre-trained Convolutional Neural Network (CNN) model for classifying audio features extracted from the tracks.
- **SVM Model**: A machine learning model used to classify audio features into genres.
- **Librosa**: A Python library for extracting audio features from music files.

## Installation

### Prerequisites

Make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (v3.8 or later)
- [Node.js](https://nodejs.org/) (v14 or later)
- [Angular CLI](https://angular.io/cli) (Install with `npm install -g @angular/cli`)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) (Install with `pip install flask`)
- [Librosa](https://librosa.org/) (Install with `pip install librosa`)

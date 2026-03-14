Multi-Modal AI System for Parkinson’s Disease Detection

An AI-powered healthcare diagnostic support system designed for early Parkinson’s Disease detection using multi-modal analysis of voice recordings and drawing patterns. The system combines audio-based vocal analysis and image-based motor pattern recognition to improve prediction reliability and diagnostic confidence.

Overview
This project implements a Multi-Modal Machine Learning Pipeline that analyzes:

Voice recordings for vocal tremors and phonation irregularities
Spiral/Wave drawings for motor-control abnormalities and tremor patterns

The extracted features are fused and processed using a Random Forest ensemble model to predict the likelihood of Parkinson’s Disease.

Key Features
Multi-modal AI-based Parkinson’s detection
Voice analysis using MFCC feature extraction
Drawing analysis using HOG-based image feature extraction
Random Forest ensemble classification
FastAPI backend with REST APIs
React.js frontend with responsive UI
Real-time prediction workflow
PCA-based dimensionality reduction
SMOTE-based dataset balancing

Technology Stack
Backend
Python
FastAPI
Uvicorn

Frontend
React.js
Vite
Tailwind CSS

Machine Learning & Data Processing
Scikit-learn
Librosa
OpenCV
Scikit-Image
NumPy
Pandas

System Workflow

User uploads:

.wav voice recording
Spiral/Wave drawing image
Backend preprocesses the inputs:
MFCC extraction from audio
HOG feature extraction from images
Features are combined into a unified feature vector
Random Forest model performs prediction
Prediction result is returned to the frontend UI
Machine Learning Pipeline
Voice Analysis
MFCC feature extraction using Librosa
Detection of vocal instability and tremors
Drawing Analysis
HOG feature extraction using OpenCV and Scikit-Image
Analysis of handwriting tremors and motor irregularities

Classification
Random Forest ensemble model
Hyperparameter optimization using GridSearchCV
Dataset balancing using SMOTE
PCA for dimensionality reduction

Project Structure
project/
│
├── app/                  # FastAPI backend
├── frontend/             # React frontend
├── streamlit/            # Streamlit demo UI
├── models/               # Trained ML models
├── notebooks/            # Training and experimentation
├── requirements.txt
└── README.md

API Endpoints
Endpoint	Description
/pro	Multi-modal prediction
/voice	Voice-only prediction
/drawing	Drawing-only prediction

Model Performance
Achieved 94%+ prediction accuracy
Evaluated using:
Accuracy
Precision
Recall
F1-Score
Confusion Matrix

Running the Project

Backend
cd app
uvicorn app:app --reload --port 8000

Frontend
cd frontend
npm install
npm run dev

Future Improvements
Deep learning-based multi-modal models
Real-time speech analysis
Cloud deployment and scalability
Clinical dataset expansion
Explainable AI integration
Mobile application support
Conclusion

This project demonstrates the integration of Artificial Intelligence, Machine Learning, Computer Vision, Audio Signal Processing, and Full-Stack Development into a unified healthcare diagnostic support system for early Parkinson’s Disease detection.
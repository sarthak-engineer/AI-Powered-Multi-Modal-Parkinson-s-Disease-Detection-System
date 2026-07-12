# 🧠 AI-Powered Multi-Modal Parkinson's Disease Detection System

> An AI-powered healthcare diagnostic support system that leverages **Machine Learning, Computer Vision, and Audio Signal Processing** to assist in the early detection of Parkinson's Disease through **voice recordings** and **hand-drawn spiral/wave images**.

---

# 📌 Overview

Parkinson's Disease (PD) is a progressive neurological disorder that affects movement, speech, and motor coordination. Early identification of Parkinson's symptoms can support timely clinical evaluation and improve patient care.

This project presents a **Multi-Modal Artificial Intelligence System** capable of analyzing **voice recordings** and **drawing patterns** to predict the likelihood of Parkinson's Disease. Instead of relying on a single modality, the system combines information extracted from both speech and handwriting to improve prediction robustness.

The application integrates **Machine Learning, Computer Vision, Audio Signal Processing, REST APIs, and Full-Stack Web Development** into an interactive healthcare diagnostic support platform.

> **Note:** This project is intended for educational and research purposes only and should not be considered a replacement for professional medical diagnosis.

---

# 🚀 Key Features

* Multi-modal Parkinson's Disease prediction
* Voice-based analysis using MFCC feature extraction
* Drawing-based analysis using HOG feature extraction
* Combined multi-modal prediction model
* Random Forest ensemble classifier
* PCA-based feature dimensionality reduction
* SMOTE-based dataset balancing
* FastAPI REST API backend
* React.js frontend with responsive user interface
* Streamlit demo interface
* Real-time prediction workflow
* Modular API architecture
* End-to-end Machine Learning deployment

---

# 🏗️ System Architecture

```text
                           User Input

              Voice Recording (.wav)
                       │
                       ▼
            MFCC Feature Extraction
                       │
                       │
                       ▼

           Spiral/Wave Drawing Image
                       │
                       ▼
            HOG Feature Extraction
                       │
                       ▼

             Feature Fusion Pipeline
                       │
         Data Preprocessing & Scaling
                       │
      PCA Dimensionality Reduction
                       │
       Random Forest Classification
                       │
                       ▼

      Parkinson's Disease Prediction
```

---

# ⚙️ Technology Stack

## Programming Language

* Python

---

## Backend

* FastAPI
* Uvicorn

---

## Frontend

* React.js
* Vite
* Tailwind CSS

---

## Machine Learning

* Scikit-learn
* Random Forest Classifier
* PCA
* SMOTE

---

## Audio Processing

* Librosa
* NumPy

---

## Image Processing

* OpenCV
* Scikit-Image

---

## Data Processing

* Pandas
* NumPy

---

# 🧠 Machine Learning Pipeline

## 🎤 Voice Analysis

The voice analysis module processes `.wav` audio recordings by extracting **Mel-Frequency Cepstral Coefficients (MFCCs)**. These features capture speech characteristics associated with Parkinson's Disease, including vocal instability and phonation irregularities.

### Voice Processing Steps

* Audio loading
* Signal preprocessing
* MFCC extraction
* Feature normalization
* Prediction

---

## ✍️ Drawing Analysis

The drawing module analyzes spiral or wave drawings using **Histogram of Oriented Gradients (HOG)** feature extraction to identify motor-control abnormalities and tremor-related patterns.

### Drawing Processing Steps

* Image preprocessing
* Grayscale conversion
* HOG feature extraction
* Feature normalization
* Prediction

---

## 🔀 Multi-Modal Feature Fusion

The extracted voice and drawing features are combined into a unified feature vector.

The combined feature vector undergoes:

* Feature Scaling
* PCA-based Dimensionality Reduction
* Random Forest Classification

The multi-modal approach leverages complementary information from both modalities to provide more reliable predictions than using a single input source.

---

# 🔄 Prediction Workflow

```text
Upload Voice Recording
          │
          ▼

Upload Drawing Image
          │
          ▼

Feature Extraction

Voice → MFCC

Drawing → HOG
          │
          ▼

Feature Fusion
          │
          ▼

Data Preprocessing
          │
          ▼

Random Forest Model
          │
          ▼

Prediction Result
          │
          ▼

Display Result in Web Interface
```

---

# 📂 Project Structure

```text
Parkinson-Disease-Detection/

│
├── app/                     # FastAPI backend
├── frontend/                # React frontend
├── streamlit/               # Streamlit demo
├── models/                  # Trained machine learning models
├── notebooks/               # Training & experimentation notebooks
├── datasets/                # Dataset (if included)
├── images/                  # Screenshots and assets
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🌐 API Endpoints

| Endpoint   | Description                          |
| ---------- | ------------------------------------ |
| `/voice`   | Voice-based Parkinson's prediction   |
| `/drawing` | Drawing-based Parkinson's prediction |
| `/pro`     | Multi-modal Parkinson's prediction   |

---

# 📊 Model Performance

The final model demonstrated strong predictive performance during evaluation.

| Metric    | Value                      |
| --------- | -------------------------- |
| Accuracy  | 94%+                       |
| Precision | *Update with actual value* |
| Recall    | *Update with actual value* |
| F1-Score  | *Update with actual value* |

Evaluation methods:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

# 💻 Installation

Clone the repository

```bash
git clone <repository-url>
cd Parkinson-Disease-Detection
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Backend

```bash
cd app

uvicorn app:app --reload --port 8000
```

---

# ▶️ Running the Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🧪 Running the Streamlit Demo

```bash
cd streamlit

streamlit run app.py
```

---

# 📷 Application Workflow

1. Upload a voice recording (`.wav`)
2. Upload a spiral or wave drawing image
3. Backend extracts MFCC features from the audio
4. Backend extracts HOG features from the image
5. Features are combined into a unified representation
6. The trained Random Forest model generates a prediction
7. Prediction result is displayed through the React interface

---

# 🎯 Applications

* AI-assisted healthcare research
* Parkinson's Disease screening support
* Educational Machine Learning projects
* Computer Vision applications
* Audio Signal Processing applications
* Healthcare AI demonstrations
* Full-Stack AI deployment reference

---

# 📈 Future Improvements

* Deep Learning-based multi-modal models
* CNN and Transformer-based architectures
* Real-time speech analysis
* Explainable AI (SHAP/LIME)
* Cloud deployment
* Docker containerization
* Mobile application support
* Clinical dataset expansion
* Continuous model improvement
* Integration with electronic health systems

---

# 🛡️ Disclaimer

This project is developed **solely for educational, research, and demonstration purposes**.

The predictions generated by this system **should not be considered a medical diagnosis** and must **not replace professional clinical evaluation or consultation with qualified healthcare professionals**.

---

# 👨‍💻 Author

**Sarthak B.C.**

AI/ML Engineer | Python | Machine Learning | Deep Learning | Generative AI

* [LinkedIn](https://www.linkedin.com/in/sarthak-gowda-886b62269)


---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.

Your support is greatly appreciated!

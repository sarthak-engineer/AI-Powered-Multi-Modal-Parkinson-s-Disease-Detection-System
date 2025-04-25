# Parkinson's Disease Detection using Multimodal Data

This project implements a multimodal approach to detect Parkinson's disease using both voice recordings and handwritten drawings. The system combines features extracted from voice samples and images to provide a more accurate diagnosis.

## Project Overview

Parkinson's disease is a progressive nervous system disorder that affects movement. Early detection can significantly improve treatment outcomes. This project uses machine learning to analyze:

1. **Voice recordings** - Extracting acoustic features that may indicate Parkinson's disease
2. **Handwritten drawings** - Analyzing tremors and patterns in handwriting that are characteristic of Parkinson's disease

## Repository Structure

- `multimodal.ipynb` - Main notebook for multimodal model training and evaluation
- `voice_detection.ipynb` - Notebook for voice-based Parkinson's detection
- `img_detection.ipynb` - Notebook for image-based Parkinson's detection
- `parkinson project demo with api/` - Complete application with API backend and Streamlit frontend
  - `app/` - FastAPI backend
  - `streamlit/` - Streamlit frontend
  - `run_project.bat` - Script to run both backend and frontend

## Technologies Used

- **Data Processing**: Python, Pandas, NumPy
- **Machine Learning**: Scikit-learn, TensorFlow/Keras
- **Feature Extraction**: Librosa (audio), OpenCV & scikit-image (images)
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Visualization**: Matplotlib, Seaborn

## Model Performance

The multimodal approach achieved:
- Accuracy: 89.09%
- Precision: 100%
- Recall: 86.05%
- F1 Score: 92.5%

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip

### Setup Instructions

1. Clone the repository:
 ```
 git clone https://github.com/EbrahimMassrie963/parkinsons-disease-detection.git 
 cd parkinsons-disease-detection
 cd parkinson project demo with api

```


2. Create and activate a virtual environment:

```
python -m venv venv
venv\Scripts\activate

```

3. Install the required packages:

```
pip install -r requirements.txt

```

### Running the Application

To run the complete application with both backend and frontend:

```
cd "parkinson project demo with api"
run_project.bat

```

This will start:
- FastAPI backend on http://127.0.0.1:8000
- Streamlit frontend on http://localhost:8501

## Usage

1. Open the Streamlit application in your browser
2. Upload a voice recording (.wav file)
3. Upload a handwritten drawing image (.png or .jpg)
4. Click "Predict" to get the diagnosis result

## Notebooks

If you want to explore the model development process:

- `multimodal.ipynb` - Contains the complete multimodal approach
- `voice_detection.ipynb` - Focuses on voice-based detection
- `img_detection.ipynb` - Focuses on image-based detection

## License

Copyright (c) 2025 Ebrahim Massrie

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgements

- The Parkinson's voice dataset used in this project is from the UCI Machine Learning Repository: [Parkinson Dataset](https://archive.ics.uci.edu/ml/datasets/parkinsons)
- The handwritten spiral drawings dataset is based on research by Zham et al. on "A digital assessment system for evaluating Parkinson's disease"
- Thanks to the scikit-learn, TensorFlow, and FastAPI communities for their excellent documentation and tools
- Special thanks to all researchers working on early detection methods for Parkinson's disease

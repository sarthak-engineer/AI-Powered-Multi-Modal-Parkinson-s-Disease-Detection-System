import os
import joblib
import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from utils import extract_img_features, extract_voice_features 

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Load pre-trained model
MODEL_PATH = os.getenv("MODEL_PATH")
if not MODEL_PATH:
    raise RuntimeError("MODEL_PATH environment variable is not set.")

try:
    loaded_model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

@app.post("/pro")
async def predict_parkinsons(audio: UploadFile = File(...), image: UploadFile = File(...)):
    try:
        # Save uploaded files temporarily
        uploads_dir = "app/temp"
        os.makedirs(uploads_dir, exist_ok=True)

        audio_path = os.path.join(uploads_dir, audio.filename)
        image_path = os.path.join(uploads_dir, image.filename)

        with open(audio_path, "wb") as audio_file:
            audio_file.write(await audio.read())

        with open(image_path, "wb") as image_file:
            image_file.write(await image.read())

        # Extract features
        voice_features = extract_voice_features(audio_path)
        img_features = extract_img_features(image_path)

        # Concatenate features
        model_input = np.concatenate((voice_features, img_features), axis=1)

        # Make prediction
        prediction = loaded_model.predict(model_input)[0]
        confidence = max(loaded_model.predict_proba(model_input)[0])

        # Cleanup temporary files
        os.remove(audio_path)
        os.remove(image_path)

        # Return prediction
        return JSONResponse(content={
            "prediction": "Positive" if prediction == 1 else "Negative",
            "confidence": confidence
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

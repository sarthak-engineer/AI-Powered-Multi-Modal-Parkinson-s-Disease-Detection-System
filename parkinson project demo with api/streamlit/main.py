import streamlit as st
import requests
from PIL import Image
import io
import base64

# Configure the page
st.set_page_config(
    page_title="Parkinson's Disease Prediction",
    page_icon="🧠",
    layout="centered",
)

# Add custom CSS for dark mode styling
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .stText, .stMarkdown, .stButton, .stSelectbox, .stFileUploader, .stSlider, .stRadio, .stCheckbox, .stDownloadButton {
        color: white;
    }
    .stTitle {
        color: #00FF00;
    }
    .stSidebar {
        background-color: #121212;
        color: white;
    }
    .stSidebar .stImage {
        background-color: #121212;
    }
    .stButton>button {
        background-color: #FF5722;
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #FF7043;
    }
    .stFileUploader {
        background-color: #333333;
        border-radius: 5px;
    }
    .stFileUploader input {
        color: white;
    }
    .stTextInput>input {
        color: white;
        background-color: #333333;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True
)

# Helper function to encode images in Base64
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Paths for assets
parkinson_image_path = "C:\\Users\\Ebrahim\\Downloads\\parkinson project demo\\streamlit\\assets\\images\\parkinson.jpg"
audio_icon_path = "C:\\Users\\Ebrahim\\Downloads\\parkinson project demo\\streamlit\\assets\\images\\audio_icon.png"
image_icon_path = "C:\\Users\\Ebrahim\\Downloads\\parkinson project demo\\streamlit\\assets\\images\\image_icon.png"

# Load images
parkinson_image = Image.open(parkinson_image_path)
audio_icon_base64 = encode_image(audio_icon_path)
image_icon_base64 = encode_image(image_icon_path)

# Sidebar with information
with st.sidebar:
    st.image(parkinson_image, use_container_width=True)
    st.markdown("### About Parkinson's Disease")
    st.write(
        "Parkinson's disease is a progressive nervous system disorder that affects movement. "
        "Early detection and diagnosis can help manage symptoms more effectively."
    )

# Main title and description
st.title("🧠 Parkinson's Disease Prediction")
st.markdown(
    "<div style='text-align: center; font-size: 18px;'>"
    "Upload an audio file and a drawing image to check for Parkinson's Disease."
    "</div>",
    unsafe_allow_html=True,
)

# Input form with icons
st.markdown(
    f"<div style='display: flex; align-items: center; margin-bottom: 10px;'>"
    f"<img src='data:image/png;base64,{audio_icon_base64}' alt='Audio Icon' style='width: 24px; margin-right: 8px;'>"
    f"<label for='audio_file' style='color: white;'>Audio File</label>"
    "</div>",
    unsafe_allow_html=True,
)
audio_file = st.file_uploader(
    "Upload an audio file (.wav)",
    type=["wav"],
    label_visibility="collapsed",
    accept_multiple_files=False,
    help="Upload an audio recording in WAV format."
)

st.markdown(
    f"<div style='display: flex; align-items: center; margin-bottom: 10px;'>"
    f"<img src='data:image/png;base64,{image_icon_base64}' alt='Image Icon' style='width: 24px; margin-right: 8px;'>"
    f"<label for='image_file' style='color: white;'>Drawing Image</label>"
    "</div>",
    unsafe_allow_html=True,
)
image_file = st.file_uploader(
    "Upload a drawing image (.png, .jpg)",
    type=["png", "jpg"],
    label_visibility="collapsed",
    accept_multiple_files=False,
    help="Upload a drawing image in PNG or JPG format."
)

# Prediction button
if st.button("Predict"):
    if audio_file and image_file:
        files = {
            "audio": ("audio.wav", audio_file.getvalue(), "audio/wav"),
            "image": ("image.png", image_file.getvalue(), "image/png"),
        }
        try:
            response = requests.post("http://127.0.0.1:8000/predict", files=files)
            if response.status_code == 200:
                result = response.json()
                if result['prediction'] == "Positive":
                    st.markdown(
                        "<div style='text-align: center; margin-top: 20px;'>"
                        "<h2 style='color: red;'>Prediction: You may have Parkinson's Disease.</h2>"
                        "<p style='color: Black; font-size: 24px;'>Confidence: {:.2f}</p>"
                        "</div>".format(result['confidence']),
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        "<div style='text-align: center; margin-top: 20px;'>"
                        "<h2 style='color: green;'>Prediction: You are unlikely to have Parkinson's Disease.</h2>"
                        "<p style='color: Black; font-size: 24px;'>Confidence: {:.2f}</p>"
                        "</div>".format(result['confidence']),
                        unsafe_allow_html=True,
                    )
                # Display audio player
                st.audio(audio_file)
                # Display image
                image = Image.open(io.BytesIO(image_file.getvalue()))
                st.image(image, caption="Uploaded Drawing", use_container_width=True)
            else:
                st.error(f"Error: {response.json()['detail']}")
        except Exception as e:
            st.error(f"Request failed: {e}")
    else: 
        st.error("Please upload both audio and image files.")



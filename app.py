import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import os

#model loading
model = tf.keras.models.load_model("malaria-classifier.keras")

#functions
def preprocess(img):
    img = img.resize((128,128))
    img = np.array(img) / 255.0
    return np.expand_dims(img, axis=0)

def predict_image(img):
    arr = preprocess(img)
    pred = model.predict(arr)[0][0]
    return "UNINFECTED" if pred > 0.5 else "INFECTED"

def cover_fit(img, size=150):
    img = ImageOps.fit(img, (size, size), method=Image.Resampling.LANCZOS)
    return img

#ui layout
st.set_page_config(page_title="Malaria Cell Classifier")
st.title("Malaria Cell Classifier")
st.write("Upload or try an image below")

st.markdown("---")

#prediction section
st.subheader("Prediction")

prediction_col1, prediction_col2 = st.columns([1, 2])
with prediction_col1:
    st.write("**Selected Image:**")
    display_image_slot = st.empty()

with prediction_col2:
    st.write("**Result:**")
    result_slot = st.empty()

#topbar input (upload)
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB")
    display_image_slot.image(img, width=250)
    result_slot.success(predict_image(img))

st.markdown("---")

#sample image section
st.subheader("Sample Images")
st.write("Click any image to classify it.")

sample_dir = "samples"

# Collect sample image paths
samples = []
for cls in ["infected", "uninfected"]:
    folder = os.path.join(sample_dir, cls)
    if os.path.exists(folder):
        for fname in os.listdir(folder):
            if fname.lower().endswith((".png", ".jpg", ".jpeg")):
                samples.append((os.path.join(folder, fname), cls))

# Display in grid
cols = st.columns(5)
for idx, (path, cls) in enumerate(samples):
    col = cols[idx % 5]
    with col:
        img = Image.open(path).convert("RGB")
        fitted_img = cover_fit(img)

        st.image(fitted_img, caption=cls.capitalize(), use_container_width=True)

        if st.button(f"Select", key=f"btn_{idx}"):
            display_image_slot.image(img, width=250)
            result_slot.success(predict_image(img))

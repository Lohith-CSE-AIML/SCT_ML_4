import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("hand_gesture_model.keras")

# Class names
class_names = [
    "01_palm",
    "02_l",
    "03_fist",
    "04_fist_moved",
    "05_thumb",
    "06_index",
    "07_ok",
    "08_palm_moved",
    "09_c",
    "10_down"
]

# Confidence threshold
confidence_threshold = 0.70

# Title
st.title("🤟 Hand Gesture Recognition")

st.write(
    "Upload a hand gesture image and let the CNN predict the gesture."
)

st.info(
    "📌 For the best results, upload images that are similar "
    "to the training dataset: grayscale images with a similar "
    "background, hand position, and image style."
)

# Upload image
uploaded_file = st.file_uploader(
    "Upload a hand gesture image",
    type=["jpg", "jpeg", "png"]
)

# If image uploaded
if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Display original image
    st.image(
        image,
        caption="Uploaded Image"
    )

    # Convert to grayscale
    image = image.convert("L")

    # Resize
    image = image.resize((128, 128))

    # Convert to NumPy array
    image_array = np.array(image)

    # Normalize pixels
    image_array = image_array / 255.0

    # Add channel dimension
    image_array = np.expand_dims(
        image_array,
        axis=-1
    )

    # Add batch dimension
    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # Prediction
    prediction = model.predict(
        image_array,
        verbose=0
    )

    # Get predicted class
    predicted_class = np.argmax(
        prediction[0]
    )

    # Get confidence
    confidence = np.max(
        prediction[0]
    )

    # Display result
    st.subheader("Prediction")

    # Check confidence
    if confidence >= confidence_threshold:

        st.write(
            f"Gesture: **{class_names[predicted_class]}**"
        )

        st.write(
            f"Confidence: **{confidence * 100:.2f}%**"
        )

    else:

        st.warning(
            "Unable to confidently recognize this gesture."
        )
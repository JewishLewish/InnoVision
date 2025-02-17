import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np


def main():
    # Open the file in read mode
    #with open('requrements.txt', 'r') as file:
    #    # Read the contents of the file
    #    data = file.read()
    # Why read requirements.txt? If you are trying to use it then it's better if you made try or except at the imports


    model = tf.keras.models.load_model('C:/Users/vikas/Downloads/neuralnetwork.h5')

    st.title("Burmese Handwriting to Text Recognition")

    uploaded_file = st.file_uploader("Choose a handwritten Burmese text image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Preprocess the image
        img = image.load_img(uploaded_file, target_size=(100, 100))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0

        # Make prediction
        prediction = model.predict(img_array)

        # Display the uploaded image
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Display the predicted class
        st.subheader("Prediction:")
        st.write(f"The predicted class is: {np.argmax(prediction)}")

        # Display the probabilities for each class
        st.subheader("Class Probabilities:")
        st.write(prediction)

if __name__ == "__main__":
    main()
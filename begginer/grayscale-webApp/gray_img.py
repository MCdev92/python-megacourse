import streamlit as st
from PIL import Image


st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera, take photo button added by default
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)
    
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")
    
    # Render the grayscale image on the webpage
    st.image(gray_img)
    
    # Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.image(gray_uploaded_img)
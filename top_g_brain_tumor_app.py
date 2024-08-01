# -*- coding: utf-8 -*-
"""Top G Brain Tumor App.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MHXo6yR22OF1D9u7EdhzaDoZr0Oo_95R
"""


# Commented out IPython magic to ensure Python compatibility.

import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuration
API_KEY = 'AIzaSyAyGrTbjkU6cGEVSOZB5z4E044GuNY4Z-Q'
MODEL_NAME = 'gemini-1.5-flash'

INPUT_PROMPT = """
You are an expert in understanding MRI images of the brain. 
You will receive input images as MRI images of the brain, 
and you will describe any visual features that might indicate abnormalities or tumor-like structures. 
Please focus on describing shapes, spots, patterns, or any unusual characteristics you observe.
"""

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)
chat = model.start_chat(history=[])

# Functions

# instantiating the gemini model 
def get_gemini_response(input_text, images, prompt):
    response = model.generate_content([input_text] + images + [prompt])
    return response.text

# creating a function to load images properly
def input_image_setup(uploaded_files):
    if uploaded_files:
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": uploaded_file.getvalue()
            }
            for uploaded_file in uploaded_files
        ]
        return image_parts
    else:
        raise FileNotFoundError("No files uploaded")

# Streamlit App Configuration
st.set_page_config(page_title="Brain Tumor Detection")

# Streamlit App
st.header("Top G Brain Tumor App 🧠")

uploaded_files = st.file_uploader("Choose images...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_column_width=True)

input_text = st.text_input("Input prompt:", key="input")

submit = st.button("Analyze MRI Images..")

if submit:
    if not uploaded_files:
        st.info("Please upload at least one image")
    else:
        try:
            image_data = input_image_setup(uploaded_files)
            response = get_gemini_response(input_text, image_data, INPUT_PROMPT)
            st.subheader("The Response is")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
 
# 
# 
#














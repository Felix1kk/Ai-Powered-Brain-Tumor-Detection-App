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
 
API_KEY='AIzaSyAyGrTbjkU6cGEVSOZB5z4E044GuNY4Z-Q'
genai.configure(api_key=API_KEY)
 
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
 
 
def get_gemini_response(input,image,prompt):
  #Loading the Gemini Model
 
  model=genai.GenerativeModel('gemini-pro-vision')
  response=model.generate_content([input,image[0],prompt])
  return response.text
# 
# 
def input_image_setup(uploaded_file):
   if uploaded_file is not None:
     # Read the file into bytes
     bytes_data =uploaded_file.getvalue()
# 
     image_parts =[
         {
             "mime_type": uploaded_file.type,
             "data": bytes_data
         }
     ]
     return image_parts
   else :
     raise FileNotFoundError("No file uploaded")
 
 
st.set_page_config(page_title="Brain Tumor detection")
 
 # Building the streamlit application
 
st.header("Top G Brain Tumor App 🧠")
 
uploaded_file=st.file_uploader("choose an image...",type=["jpg","jpeg","png"])
 
image=""
if uploaded_file is not None:
  image=Image.open(uploaded_file)
  st.image(image,caption="uploaded Image.",use_column_width=True)
 
input=st.text_input("input prompt: ",key="input")
 
submit=st.button("Tell me about the tumor")
 
input_prompt="""
You are an expert in understanding Mri images. You wil
receive input images as mri images of the brain and you will have to
classify what type of tumor it is. if it is not a tumor return No tumor
"""
if submit and uploaded_file is None or uploaded_file=="":
  st.info("Please upload an Image")

elif submit and uploaded_file is not None:
  image_data=input_image_setup(uploaded_file)
  response=get_gemini_response(input_prompt,image_data,input)
 
  st.subheader("The Response is")
  st.write(response)
 
# 
# 
#














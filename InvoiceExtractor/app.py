from dotenv import load_dotenv
load_dotenv() ## Load the .env file- environment variables

import streamlit as st
import os
import google.generativeai as genai
import PIL.Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#  function to load gemini model and responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image, prompt):
    response =  model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, # get the mime type of the file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# initialize the stremlit app
st.set_page_config(page_title="Multi Language Invoice Extractor", page_icon="🧠", layout="wide")
st.header("Multi Language Invoice Extractor")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"], key="image")
image = ""
if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width =True)

submit = st.button("Extract Invoice Information")

input_prompt = """
You are an expert in invoice extraction. You have been asked to extract the following information from the invoice:
"""

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The response is:")
    st.write(response)
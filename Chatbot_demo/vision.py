from dotenv import load_dotenv
load_dotenv() ## Load the .env file- environment variables

import streamlit as st
import os
import google.generativeai as genai
import PIL.Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#  function to load gemini model and responses
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(input,image):
    if input!= "":
        response =  model.generate_content([input,image])
    else:
        response =  model.generate_content(image)
    return response.text


# initialize the stremlit app

st.set_page_config(page_title="Gemini Image Demo", page_icon="🧠", layout="wide")
st.header("Gemini Image Application")


input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"], key="image")
image = ""
if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width =True)
else:
    image = None

submit = st.button("Tell me about the image:")


## When submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is:")
    st.write(response)
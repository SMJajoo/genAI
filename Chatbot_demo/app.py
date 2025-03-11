from dotenv import load_dotenv
load_dotenv() ## Load the .env file- environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#  function to load gemini model and responses
model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_response(question):
    response =  model.generate_content(question)
    return response.text

# initialize the stremlit app

st.set_page_config(page_title="Q&A", page_icon="🧠", layout="wide")

st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")


## When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
import streamlit as st

genai.configure(api_key=os.getenv('GENAI_API_KEY'))

#function to load gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_reponse(question):
    response = chat.send_message(question, stream = True)
    return response

st.set_page_config(page_title="Chatbot Demo", page_icon="🤖", layout="wide")
st.header("Gemini LLM Chatbot")

# Initialize session state for chat history if it doesnt exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

input_text = st.text_input("Input: ",key="input_text")
submit = st.button("Submit")

if submit and input_text:
    response = get_gemini_reponse(input_text)
    # Add user query and response to session chat history
    st.session_state["chat_history"].append(("You",input_text))
    st.subheader("The response is:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Gemini",chunk.text))

st.subheader("Chat History is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
load_dotenv()

st.set_page_config(
    page_title="Ask Rick Sanchez!",
    page_icon=":rocket:", 
    layout="wide", 
)

API_KEY = os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

def assignRole(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title(" Rick Sanchez ChatBot 👨🏻‍🔬")

for message in st.session_state.chat_session.history:
    with st.chat_message(assignRole(message.role)):
        st.markdown(message.parts[0].text)

user_prompt = st.chat_input("Ask Rick anything you want")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    geminiReply = st.session_state.chat_session.send_message("Answer this as Rick Sanchez from Rick and Morty without any explicit content"+" "+user_prompt)
    with st.chat_message("assistant"):
        st.markdown(geminiReply.text)

        


import streamlit as st
import requests

# Define the API URL
API_URL = "http://localhost:8000/chat"

# Streamlit user interface
st.title("Chatbot App with Google Gemini LLM")

user_input = st.text_input("You: ", "Hello, how can I help you?")
if st.button("Send"):
    if user_input:
        response = requests.post(API_URL, json={"query": user_input})
        st.text(f"Chatbot: {response.json().get('response')}")
    else:
        st.text("Please enter a query.")

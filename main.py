from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('GOOGLE_API_KEY')

# API key Configuration
genai.configure(api_key=api_key)

# Initialization of model
model = genai.GenerativeModel('gemini-1.5-pro-latest')

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

# Function to get response from the Gemini model
def get_response_from_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

@app.post("/chat")
async def chat(request: QueryRequest):
    response_text = get_response_from_gemini(request.query)
    return {"response": response_text}

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.header("Ask Me App")

prompt = st.text_area("Ask Anything")

def getAnswer(prompt):
    llm=ChatGoogleGenerativeAI(model="gemini-pro", temperature=1.0, google_api_key=os.getenv("API_KEY"))
    result = llm.invoke(prompt)
    st.write(result.content)

if st.button("Ask Me"):
    getAnswer(prompt)

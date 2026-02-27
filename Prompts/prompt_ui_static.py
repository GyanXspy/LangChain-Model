from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

st.header("Research Tool")
user_input = st.text_input("Enter Prompt")

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

if st.button("Summerize"):
    result = model.invoke(user_input)
    if isinstance(result.content, list):
        text_output = ""
        for block in result.content:
            if isinstance(block, dict) and block.get("type") == "text":
                text_output += block.get("text", "")
        st.write(text_output)

    else:
        st.write(result.content)
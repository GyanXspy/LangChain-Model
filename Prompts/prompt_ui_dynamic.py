from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate , load_prompt

from dotenv import load_dotenv
load_dotenv()
import streamlit as st

st.header("Research Tool")
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')
prompt = template.invoke(
    {
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    }
)

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

if st.button("Summerize"):
    result = model.invoke(prompt)
    if isinstance(result.content, list):
        text_output = ""
        for block in result.content:
            if isinstance(block, dict) and block.get("type") == "text":
                text_output += block.get("text", "")
        st.write(text_output)

    else:
        st.write(result.content)
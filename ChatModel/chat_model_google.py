from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

mod = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')
result = mod.invoke("What is the capital of India?")
print(result.content)
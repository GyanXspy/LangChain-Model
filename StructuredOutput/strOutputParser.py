from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()


llm = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=4) # this load the chatgpt chat model and temperature for how creative ans you want and max_completion_tokens for how many token you want
result = llm.invoke("What is the capital of India")
print(result)
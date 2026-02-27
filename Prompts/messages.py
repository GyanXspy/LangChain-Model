from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

result = model.invoke(messages)
# Extract text safely
if isinstance(result.content, list):
    text = "\n".join(
        block["text"]
        for block in result.content
        if isinstance(block, dict) and block.get("type") == "text"
    )
else:
    text = result.content

# Append clean AI message
messages.append(AIMessage(content=text))

print(messages)



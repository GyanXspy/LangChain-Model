from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))

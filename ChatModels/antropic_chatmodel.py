from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from anthropic import Anthropic
import os

# explicitly tell dotenv where your .env is located
load_dotenv(dotenv_path="/Users/hasebul/langChain_Models/.env")

# Use a valid model name from your list
model = ChatAnthropic(model="claude-sonnet-4-5-20250929")

response = model.invoke("Who wrote 'Romeo and Juliet'?")
print(response.content)

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv(dotenv_path="/home/hasebul/langChain_Models/.env")

model = ChatAnthropic(model="claude-sonnet-4-5-20250929")

response = model.invoke("Who wrote 'Romeo and Juliet'?")
print(response.content)

from langchain_anthropic import ChatAnthropic
from typing import Literal, TypedDict
from dotenv import load_dotenv

load_dotenv()
class Review(TypedDict):
    summary: str
    sentiment: Literal["good", "better", "best"] 
    
model = ChatAnthropic(model='claude-sonnet-4-5-20250929')
structured_output_model = model.with_structured_output(Review)

result = structured_output_model.invoke("""The AuraSilence Pro headphones are a solid choice for everyday use. The sound quality is clear, especially the mid-tones, and the battery life easily gets me through a full workday. The noise-canceling feature works well enough to mute consistent background hums, like on an airplane or bus. They are comfortable for a few hours at a time, and the controls are easy to find. While they might not completely block out loud, sudden noises, they definitely make my commute much more pleasant. A good, reliable pair of headphones
""")

print(result)



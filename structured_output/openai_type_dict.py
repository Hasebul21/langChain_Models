from typing import Literal, TypedDict, Annotated
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class Review(TypedDict):
    rating: Annotated[str, "Tell me overall rating between good, better , best"]
    pros: Annotated[str, "tell me about the advantage of buying one in 2-3 sentence"]
    cons: Annotated[str, "tell me about the disadvantage of buying one in 2-3 sentence"]



model = ChatOpenAI(model='gpt-4o-mini')
structured_output_model = model.with_structured_output(Review)

result1 = structured_output_model.invoke("""The iPhone 16 series brings several notable upgrades centered on performance, design, and new user controls. All models are powered by the new A18 chip, offering significant speed and efficiency improvements over previous generations, especially in supporting new AI features. This new performance is crucial for utilizing Apple Intelligence, the company's suite of generative AI capabilities integrated throughout the operating system, which includes advanced writing tools, image generation, and a smarter Siri.A key physical design change for the standard iPhone 16 and 16 Plus is the new vertical rear camera layout. This switch from the previous diagonal arrangement allows the base models to record Spatial Video, a format that captures three-dimensional depth for viewing on devices like the Apple Vision Pro. The camera system itself receives an upgrade, featuring an advanced 48-megapixel Main camera and an improved Ultra Wide camera for better low-light performance.For enhanced user interaction, the iPhone 16 introduces two new physical buttons. The Action Button, previously exclusive to the Pro models, is now included on the standard iPhone 16 and 16 Plus, providing a customizable shortcut to various functions. Additionally, all models gain a dedicated Camera Control Button on the side, designed to make photography and videography feel more like using a dedicated camera, offering press-and-half-press functionality for focus and a quick way to launch and control the camera app.Finally, the Pro models of the iPhone 16 see an increase in screen size, with the iPhone 16 Pro and Pro Max becoming slightly larger to accommodate new internal components and displays. Across the entire lineup, the phones are expected to feature support for Wi-Fi 7 and offer enhanced battery life, addressing common user desires for faster connectivity and greater endurance. These changes represent a blend of subtle refinements and significant hardware additions to the iPhone experience
""")

print(f"Rating: {result1['rating']}")
print(f"Pros: {result1['pros']}")
print(f"Cons: {result1['cons']}\n")

result2 = structured_output_model.invoke("""The Samsung Galaxy S22 Ultra effectively merged the best elements of the Galaxy S series and the defunct Note series, making it the company’s ultimate productivity and power flagship. Its design echoes the sharp, monolithic aesthetic of the Note line, complete with a dedicated silo for the S Pen stylus. This S Pen is a major highlight, featuring a dramatically reduced latency of just 2.8ms, making writing and drawing feel almost instantaneous and perfectly natural. This deep integration makes the S22 Ultra a versatile tool for both creatives and power users who rely on precise input and note-taking.Powering the device is either the Snapdragon 8 Gen 1 or Exynos 2200 chipset (depending on the region), delivering a top-tier performance capable of handling demanding games and heavy multitasking, though it can run warm under sustained load. This power drives a magnificent 6.8-inch Dynamic AMOLED 2X display. With a WQHD+ resolution and a dynamic 120Hz refresh rate that can scale down to save power, the screen is renowned for its stunning brightness, color accuracy, and overall visual quality, making it one of the best available on a smartphone. The quad-camera system is another standout feature, boasting a versatile setup with a 108MP main sensor and two dedicated telephoto lenses providing 3x and 10x optical zoom, which combine to offer impressive "Space Zoom" capabilities up to 100x. The camera's strength lies not just in hardware, but in software improvements like "Nightography," which enhances low-light photography and video capture to produce brighter, clearer results. While the 5,000mAh battery provides a good full day of mixed use, some users felt it did not offer a significant improvement over its predecessor. Ultimately, the S22 Ultra is defined by its comprehensive feature set, combining the best camera hardware with the unique, integrated S Pen for an unmatched Android experience at the premium end of the market
""")

print(f"Rating: {result2['rating']}")
print(f"Pros: {result2['pros']}")
print(f"Cons: {result2['cons']}")


class Decision(TypedDict):
    name : Annotated[str, "Tell me model which one user should buy"]
    purpose: Annotated[str, "explain why a user should by that model"]


# Create a comparison prompt using the previous results
comparison_prompt = f"""
Compare these two phones and suggest which one to buy.

Return your answer strictly as a JSON object using these exact field names:
- name: the model the user should buy
- purpose: explanation why that model is better

Phone 1 (iPhone 16):
Rating: {result1['rating']}
Pros: {result1['pros']}
Cons: {result1['cons']}

Phone 2 (Samsung S22 Ultra):
Rating: {result2['rating']}
Pros: {result2['pros']}
Cons: {result2['cons']}
"""

structured_output_model_decision = model.with_structured_output(Decision)
result = structured_output_model_decision.invoke(comparison_prompt)

try:
    print(f"\nFinal Recommendation:")
    print(f"Recommended Phone: {result['name']}")
    print(f"Reason: {result['purpose']}")
except KeyError as e:
    print(f"Error accessing result: {e}")
    print("Raw result:", result)
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # pip install openai



user_prompt = "cat wearing red cape"


response = client.images.generate(prompt=user_prompt,
n=1,
size="1024x1024")
image_url = response.data[0].url
print(image_url)

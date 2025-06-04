"""
トライやるウィーク用
012
"""

import openai

client = openai.OpenAI(api_key="XXXXXXXXX")
response = client.images.generate(
    model="dall-e-3",
    prompt="2つのダイヤモンド",
    size="1024x1024",
    quality="hd",
    n=1,
)

image_url = response.data[0].url
print(image_url)

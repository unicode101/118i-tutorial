import openai
from openai import OpenAI
import os
import base64
import requests
import streamlit as st

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

uploaded_file = st.file_uploader("Choose a picture file", type=["png", "jpg", "jpeg"])

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

image_path = "images/cloud.png"

def photo_rec(image_path):
    base64_image = encode_image(image_path)
    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "What’s in this image in terms of food?"},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}",
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )
    return response.choices[0].message.content


if uploaded_file is not None:
    with open(os.path.join('images',uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success("Saved File:{} to images".format(uploaded_file.name))
    image_path = os.path.join('images',uploaded_file.name)
    st.image(image_path)
    content = photo_rec(image_path)
    st.write(content)

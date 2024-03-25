import openai

import os
import openai
import streamlit as st
import requests
from openai import OpenAI

st.markdown("# Page 4 ❄️")
st.sidebar.markdown("# Page 4 ❄️")

# Create two radio buttons
source_language = st.radio('Source language', ['English', 'French', 'German'])
target_language = st.radio('Target language', ['English', 'French', 'German'])

# Create a text input field
text = st.text_input('Enter what you want to translate')

# Create a button
if st.button('Submit'):
    # Print the input from the text field and radio buttons
    st.write(f'You entered: {text}')
    st.write(f'Source language: {source_language}')
    st.write(f'Target language: {target_language}')

"""
openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def translate(text, source_language = "English", target_language = "French"):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Translate the following " + source_language + " text to "+target_language+": {text}",
        temperature=0.5,
        max_tokens=60
    )
    return response.choices[0].text.strip()

print(response.choices[0].text.strip())

"""
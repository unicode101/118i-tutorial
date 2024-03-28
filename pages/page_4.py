import openai
import os
import openai
import streamlit as st
import requests
from openai import OpenAI

st.markdown("# Page 4: Translation ❄️")
st.sidebar.markdown("# Page 4: Translation ❄️")

# Create two radio buttons
source_language = st.radio('Select Source language', ['English', 'French', 'German'])
target_language = st.radio('Select Target language', ['English', 'French', 'German'])

# Create a text input field
text = st.text_input('Enter the text you want to translate: ')

# Create a button
if st.button('Submit'):
    # Print the input from the text field and radio buttons
    st.write(f'You entered: {text}')
    st.write(f'Source language: {source_language}')
    st.write(f'Target language: {target_language}')


openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()


def translate(text, source_language = "English", target_language = "French"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You will be provided with a sentence in "+ source_language
                +", and your task is to translate it into " + target_language 
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    
    return response.choices[0].message.content

st.write(translate(text, source_language, target_language))
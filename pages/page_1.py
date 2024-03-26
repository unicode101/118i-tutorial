import os
import openai
import streamlit as st
from openai import OpenAI


st.markdown("# Page 1: Text Generation (Lab 2, 5, 6) ❄️")
st.sidebar.markdown("# Page 1: Text Generation ❄️")

openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()


# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": "Your job is to help me understand a concept that a 6-year-old can understand."},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

# create our streamlit app
with st.form(key = "chat"):
    prompt = st.text_input("Enter a concept you would like me to explain: ") 
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(get_completion(prompt))
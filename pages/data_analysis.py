
# The tutorial is created based on the contribution of Matthew Ignacio, MIS'23 with permission.
# The code is further reviesd with the help of GitHub Copilot
# #pip3 install pandas, requests, matplotlib, seaborn
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns

import os
import openai
import streamlit as st
from openai import OpenAI

# Load the dataset into a pandas DataFrame
data = pd.read_csv('pages/data/Data.csv')

# Display the first few rows of the DataFrame
st.write(data.head())
openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

# Calculate the mean loss percentage for each country and get the top 5
top_countries_loss = data.groupby('country')['loss_percentage'].mean().nlargest(5)

# Plot the top 5 countries with the highest loss percentage
sns.barplot(x=top_countries_loss.index, y=top_countries_loss.values)
plt.title('Top 5 Countries with Highest Loss Percentage')
plt.ylabel('Average Loss Percentage')
plt.xlabel('Country')
plt.xticks(rotation=45)

prompt = (
    f"The countries with the highest average food loss percentages are: "
    f"{', '.join(top_countries_loss.index)}. "
    "What could be the contributing factors to this high loss percentage "
    "and its implications on sustainability and food security?"
)

# create a wrapper function
def get_completion(prompt, model="gpt-3.5-turbo"):
   completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role":"system",
         "content": prompt},
        {"role": "user",
         "content": prompt},
        ]
    )
   return completion.choices[0].message.content

st.bar_chart(top_countries_loss, use_container_width=True)

st.write(get_completion(prompt))

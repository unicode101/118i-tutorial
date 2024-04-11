from youtube_transcript_api import YouTubeTranscriptApi
import urllib.parse
import streamlit as st
import os
import openai
from openai import OpenAI


def get_transcript(video_url):
    # Parse the URL and extract the video ID
    transcript_text = ""
    url_data = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(url_data.query)
    video_id = query["v"][0]

    print(video_id)  # Outputs: -uleG_Vecis

    # Get the transcript
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    # Print the transcript
    for entry in transcript:
        transcript_text += entry['text']
    
    return transcript_text

# Takes the transcription of the meeting and returns a summary of it via text completions
def abstract_summary_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content

st.markdown("#Youtube summary❄️")
st.sidebar.markdown("# Youtube summary ❄️")

openai.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

# create our streamlit app
with st.form(key = "chat"):
    url = st.text_input("Enter the Youtube link: ") 
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        VIDEO_URL = url
        st.video(VIDEO_URL)
        st.write(abstract_summary_extraction(get_transcript(url)))







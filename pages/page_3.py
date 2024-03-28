import streamlit as st
import os
import openai
from openai import OpenAI
from pathlib import Path

st.markdown("# Page 3: Transcription 🎉 (Lab 4)")
st.sidebar.markdown("# Page 3: Transcription 🎉")


openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()


# display audio based on the following tutorial:
# https://www.educative.io/answers/how-to-add-the-media-elements-to-the-streamlit-web-interface
#speech_file_path = Path(__file__).parent / 'pages/audio/Meeting_Minutes.mp3'
#audio_file_path = 'audio/Meeting_Minutes.mp3'
audio_file_path = Path(__file__).parent / 'audio/Meeting_Minutes.mp3'
audio_file = open(audio_file_path, 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')
st.write("Transcribing and Summarizing Audio file... Please wait for the results...")

# transcribe the audio 
# Given the path to an audio file, transcribes the audio using Whisper.
# For more Speech-to-text features, check:
# https://platform.openai.com/docs/guides/speech-to-text
def transcribe_audio(audio_file_path):
    audio_file = open(audio_file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription.text

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

# Takes the transcription of the meeting and returns the key points in it via text completions
def key_points_extraction(transcription):
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

# Takes the transcription of the meeting and returns the action items from it via text completions
def action_item_extraction(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are an AI expert in analyzing conversations and extracting action items. Please review the text and identify any tasks, assignments, or actions that were agreed upon or mentioned as needing to be done. These could be tasks assigned to specific individuals, or general actions that the group has decided to take. Please list these action items clearly and concisely."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content

# Takes the transcription of the meeting and returns the sentiment of it via text completions
def sentiment_analysis(transcription):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible. Please keep it to fewer than 5 sentences."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response.choices[0].message.content

# Taken directly from OpenAI's documentation for a meeting minutes generator.
def meeting_minutes(transcription):
    abstract_summary = abstract_summary_extraction(transcription)
    key_points = key_points_extraction(transcription)
    action_items = action_item_extraction(transcription)
    sentiment = sentiment_analysis(transcription)
    return {
        'abstract_summary': abstract_summary,
        'key_points': key_points,
        'action_items': action_items,
        'sentiment': sentiment
    }

transcription = transcribe_audio(audio_file_path)
minutes = meeting_minutes(transcription)
abstract_summary = "ABSTRACT SUMMARY\n" + minutes["abstract_summary"] + "\n\n"
key_points = "KEY POINTS\n" + minutes["key_points"] + "\n\n"
action_items = "ACTION ITEMS\n" + minutes["action_items"] + "\n\n"
sentiment = "SENTIMENT\n" + minutes["sentiment"] + "\n\n"

print(abstract_summary + key_points + action_items + sentiment)

st.header('Transcription results :blue[cool] :sunglasses:', divider='rainbow')

option = st.radio(
    "Select your desired output:",
    [ ":one: :rainbow[Summary]", 
     ":two: sentiment :movie_camera:",
     ":three: action_items :ballot_box_with_check:", 
     ":four: key_points :receipt:"],
    captions = [
                "See the summary of the meeting", 
                "Check out the sentiment of this meeting",
                "List action items from the meeting",
                "List key points discussed in the meeting"])

if option == ":one: :rainbow[Summary]":
    st.write(abstract_summary)
elif option == ":two: sentiment :movie_camera:":
    st.write(sentiment)
elif option == ":three: action_items :ballot_box_with_check:":
    st.write(action_items)
elif option == ":four: key_points :receipt:":
    st.write(key_points)
#st.write(transcription)
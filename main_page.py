import streamlit as st
import pandas as pd
import numpy as np
import time



st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

message = "This page provides template for Streamlit UI components! 🎉\nPlease navigate the pages to explore some sample code."
message += "Please check the Streamlit Documentation page for more componets."
st.write(message)

st.link_button("Click for more Streamlit features", "https://docs.streamlit.io/develop")



st.subheader('Slider Example', divider='grey')

# slider bar
# https://docs.streamlit.io/develop/api-reference/execution-flow/st.form

form = st.form("my_form")
slider_value = form.slider("Inside the form")
# Now add a submit button to the form:
submit_button = form.form_submit_button("Submit")
if submit_button:
    st.write(f'The slider value is: {slider_value}')

outside_slider_value = st.slider("Outside the form")
st.write(f'The slider value is: {outside_slider_value}')



st.subheader('Button to an external link Example', divider='grey')
# download button
#https://docs.streamlit.io/develop/api-reference/widgets/st.download_button


st.link_button("Click for more input widgets", "https://docs.streamlit.io/develop/api-reference/widgets")

st.subheader('Click to navigate three pages Example', divider='grey')
col1, col2, col3 = st.columns(3)
with col1:
   st.page_link("main_page.py", label="Home", icon="🏠", disabled=True)

with col2:
   st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")

with col3:
   st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣")


st.subheader('Showing three pages vertically', divider='grey')

# 
st.page_link("main_page.py", label="Home", icon="🏠", disabled=True)
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣")


st.subheader('Showing Tables', divider='grey')
# showing tables
# https://docs.streamlit.io/develop/api-reference/data/st.dataframe
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
st.link_button("Click for more dataframe examples", "https://docs.streamlit.io/develop/api-reference/data/st.dataframe")


# multiple containers
# Source: https://docs.streamlit.io/develop/api-reference/layout/st.columns
# https://docs.streamlit.io/develop/api-reference/layout
st.subheader('Showing three columns', divider='grey')
col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

st.link_button("Click for more column styles", "https://docs.streamlit.io/develop/api-reference/layout/st.columns")

st.subheader('Text Element', divider='grey')
st.link_button("Click for more text elements", "https://docs.streamlit.io/develop/api-reference/text")


st.subheader('Maps', divider='grey')
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.33, -121.88],
    columns=['lat', 'lon'])
st.map(df)
st.link_button("Click for more map examples", "https://docs.streamlit.io/develop/api-reference/charts/st.map")


st.subheader('Containers', divider='grey')

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")
st.link_button("Click for more container examples", "https://docs.streamlit.io/develop/api-reference/layout/st.container")

# charts
st.subheader('Example of charts', divider='grey')

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)
st.link_button("Click for more chart examples", "https://docs.streamlit.io/develop/api-reference/charts")

# media elements
st.subheader('Example of media elements', divider='grey')
VIDEO_URL = "https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/"
st.video(VIDEO_URL)
st.link_button("Click for more media examples", "https://docs.streamlit.io/develop/api-reference/media")

# status elements
st.subheader('Status elements', divider='grey')
col1, col2 = st.columns(2)

with col1:
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    st.button("Rerun")

with col2:
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')


st.link_button("Click for more status examples", "https://docs.streamlit.io/develop/api-reference/status")


# media elements
st.subheader('Example of chat elements', divider='grey')

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

st.link_button("Click for more chat examples", "https://docs.streamlit.io/develop/api-reference/chat")
